# MICRON
## BASH
* datablocks
```
#> Setup
pip install -e $DATABLOCKS
pip install -e $DATABLOCKS_COLLECTION

#> Define
export DATALAKE=$HOME/.cache/testlake
rm -rf $DATELAKE # optional, to ensure a clean test
export MIRLOGCOHN="datablocks.DBX('datablocks_collections.micron.micron_datablocks.miRLogCoHN', 'miRLogCoHN', verbose=True)"
export MIRCOHN="datablocks.DBX('datablocks_collections.micron.micron_datablocks.miRCoHN', 'miRCoHN', verbose=True).SCOPE(logcounts=$MIRLOGCOHN.READ())"

#> Examine
echo "$MIRLOGCOHN"
dbx "$MIRLOGCOHN"
dbx "$MIRLOGCOHN.scope"
python -c "from datablocks_collections.micron.micron_datablocks import miRLogCoHN; help(miRLogCoHN)"
python -c "from datablocks_collections.micron.micron_datablocks import miRLogCoHN; help(miRLogCoHN.SCOPE)"

dbx "$MIRCOHN"
dbx "$MIRCOHN.scope"
dbx "$MIRCOHN.intent()"
dbx "$MIRCOHN.extent()"

#> Build
#... Start with miRCoHN: upstream dependency
...

```
