$fem_type2$ = <Noun>:<> ({<singular><direct>}:{} | {<singular><oblique>}:{} |{<plural><direct>}:{iyAM} | {<plural><oblique>}:{iyoM} )

ALPHABET = [A-Za-z] [<Noun> I i iyAM iyoM]:<> 
$delete-A$ = [iyoM iyAM] <=> <> (<Noun>:<>[iyoM iyAM])

"fem_type2.lex" $fem_type2$ || $delete-A$




