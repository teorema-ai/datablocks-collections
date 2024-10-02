# MICRON
## BASH
* datablocks
```
#> Setup
pip install -e $DATABLOCKS
pip install -e $DATABLOCKS_COLLECTION

#> Env & Survey
export DATALAKE=$HOME/.cache/testlake
dbx "DBX.show_datablocks()"

#> Define DBXs
rm -rf $DATELAKE # optional, to ensure a clean test
export MIRLOGCOHN="datablocks.DBX('datablocks_collections.micron.micron_datablocks.miRLogCoHN', \
                                  'miRLogCoHN', \
                                  repo='$DATABLOCKS_COLLECTIONS',\
                                  revision='90c94374253985766c10e3ce0b60550e317622d1',\
                                  verbose=True)"
export MIRCOHN="datablocks.DBX('datablocks_collections.micron.micron_datablocks.miRCoHN', 'miRCoHN', \
                                verbose=True).SCOPE(logcounts=$MIRLOGCOHN.READ())"

#> Examine
echo "$MIRLOGCOHN"
dbx "$MIRLOGCOHN"
dbx "$MIRLOGCOHN.scope"
python -c "from datablocks_collections.micron.micron_datablocks import miRLogCoHN; help(miRLogCoHN)"
python -c "from datablocks_collections.micron.micron_datablocks import miRLogCoHN; help(miRLogCoHN.SCOPE)"
dbx "$MIRLOGCOHN.show_build_records()"
dbx.print "$MIRLOGCOHN.intent"
dbx.print "$MIRLOGCOHN.extent"
dbx.print "$MIRLOGCOHN.shortfall"
dbx.print "$MIRLOGCOHN.metric"
dbx.print "$MIRLOGCOHN.valid"

dbx "$MIRCOHN"
dbx "$MIRCOHN.show_build_records()"
dbx "$MIRCOHN.scope"
#dbx "$MIRCOHN.tagscope"
dbx "$MIRCOHN.topics"
dbx "$MIRCOHN.intent"
dbx "$MIRCOHN.extent"

#> Build
#... Start with miRCoHN: upstream dependency
...

```
