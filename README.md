# MICRON
## BASH
* datablocks
```
#> Define
export DATALAKE=$HOME/.cache/testlake
rm -rf $DATELAKE
export MIRCOHN="datablocks.DBX('datablocks_collections.micron.micron_datablocks.miRCoHN', verbose=True)"
export MIRCOSTATS="datablocks.DBX('datablocks_collections.micron.micron_datablocks.miRCoStats').SCOPE(mirco=$MIRCOHN.READ('counts'))"

#> Examine
echo "$MIRCOHN"
dbx "$MIRCOHN"
dbx "$MIRCOHN.scope"
dbx "help(datablocks_collections.micron.micron_datablocks.miRCoHN)"
dbx "help(datablocks_collections.micron.micron_datablocks.miRCoHN.SCOPE)"

dbx "$MIRCOSTATS.SCOPE"
dbx "$MIRCOSTATS.intent()"
dbx "$MIRCOSTATS.extent()"

#> Build
#... Start with miRCoHN: upstream dependency
...

```
