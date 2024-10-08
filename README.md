# MICRON
## BASH
* datablocks
```
#> Setup
pip install -e $DATABLOCKS
pip install -e $DATABLOCKS_COLLECTION
ray start --head --dashboard-host=0.0.0.0
# worker logs
ls /tmp/ray/session_latest/logs

#> Lay of the land
export DATALAKE=$HOME/.cache/testlake
dbx "DBX.show_datablocks()"
cd $DATABLOCKS_COLLECTIONS
export REVISION=`git rev-parse --short HEAD`

#> Define DBXs
rm -rf $DATELAKE # optional, to ensure a clean test
export MIRLOGCOHN="datablocks.DBX('datablocks_collections.micron.micron_datablocks.miRLogCoHN', \
                                  'miRLogCoHN', \
                                  repo='$DATABLOCKS_COLLECTIONS',\
                                  revision='$REVISION',\
                                  verbose=True).Databuilder(pool=FILE_POOL.clone(throw=True))"
export MIRCOHN="datablocks.DBX('datablocks_collections.micron.micron_datablocks.miRCoHN', 'miRCoHN', \
                                verbose=True).SCOPE(logcounts=$MIRLOGCOHN.READ())"
# validate
dbx "$MIRLOGCOHN"
dbx "$MIRCOHN"

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
