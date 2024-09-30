from dataclasses import dataclass
from typing import Tuple, List, Optional

import numpy as np
from scipy.stats import invwishart

import itertools

@dataclass
class GMM:
    """
        GMM sampler 
        - with K clusters
        - each cluster i with mean m[i] and std sigma[i] in \R^d, i = 1, ..., K
        - cluster probability p[i], i = 1, ..., K
        - total parameters \theta = [(p[i], mus[i], covs[i]) for i in range(K)]
        - p = (p[i] for i in range(K)) drawn from a symmetric Dirichlet(K, alpha) 
        - mus[i] is drawn from Guassian(d, mu, cov), 
        - covs[i] is drawn from InverseWishart(d, cov); inverse Wishart is conjugate to the distribution of covariance matrices; cov can be interpreted as a prior cov
        - priors:
            . alpha = [alpha[i] for i in range(K)]
            . mu
            . cov
        - hyperparameters:
            . d
            . K
            . seed
        - def sample(self, N):
            ...
    """
    p: np.ndarray
    mus: np.ndarray
    covs: np.ndarray
    rng: np.random.Generator
    verbose: bool = False
    debug: bool = False
                 
    @staticmethod
    def params(alpha: Tuple[int],
              mu: Optional[np.ndarray[float]] = None,
              cov: Optional[np.ndarray] = None, 
              seed: Optional[int] = None
    ):
        K = len(alpha)
        d = len(mu)
        assert d > 0, f"Non-positive d: {d}"
        assert K > 0, f"Non-positive len(alpha): {K}"
        assert cov.shape == (d, d), f"Shape of cov == {cov.shape}!= {d, d}"
        rng = np.random.default_rng(seed)

        if alpha is None:
            alpha = np.ones(K)
        if mu is None:
            mu = np.zeros(d)
        if cov is None:
            cov = np.eye(d)
        p = rng.dirichlet(alpha).transpose()
        mus = rng.multivariate_normal(mu, cov, K)
        covs = invwishart.rvs(d, cov, random_state=rng, size=K)
        return p, mus, covs, rng

    def __post_init__(self):
        K, d = self.mus.shape
        assert d > 0, f"Non-positive d: {d}"
        assert K > 0, f"Non-positive K: {K}"
        assert self.p.shape == (K,), f"p.shape == {self.p.shape} != {K,} == K"
        assert self.mus.shape == (K, d), f"mus.shape == {self.mus.shape} != {K, d} == (K, d)"
        assert self.covs.shape == (K, d, d), f"covs.shape == {self.covs.shape} != {K, d, d} == (K, d, d)"

        self._d = d
        self._K = K
        
        if self.debug:
            print(f"DEBUG: GMM: p:\n{self.p}")
            print(f"DEBUG: GMM: mus:\n{self.mus}")
            print(f"DEBUG: GMM: covs:\n{self.covs}")

    @property
    def d(self):
        return self._d
    
    @property
    def K(self):
        return self._K
        
    def sample(self, N):
        rng = self.rng
        zcounts = rng.multinomial(N, self.p, size=1)[0]
        if self.debug:
            print(f"DEBUG: GMM.sample: N: {N}, zcounts: {zcounts}")
        zslist = []
        xs = np.zeros((N, self.d))
        zcc = 0
        for k in range(self.K):
            zc = zcounts[k]
            if self.debug:
                print(f"DEBUG: GMM.sample: N: {N}, k: {k}, zc: {zc}")
            zslist += [k]*int(zc)
            xs[zcc:zcc+zc,:] = rng.multivariate_normal(self.mus[k], self.covs[k], zc)
            zcc += zc
        zs = np.array(zslist, dtype=int)
        return zs, xs
