$mas_type3$ = <Noun>:<> ({<singular><direct>}:{} | {<singular><oblique>}:{} |{<plural><direct>}:{} | {<plural><oblique>}:{oM})
% {<plural><oblique>}:{yoM} )

ALPHABET = [A-Za-z] [<Noun> a A oM yoM]:<> 
$delete-A$ = [oM yoM] <=> <> (<Noun>:<>[oM yoM]) 

"mas_type3.lex" $mas_type3$ || $delete-A$
