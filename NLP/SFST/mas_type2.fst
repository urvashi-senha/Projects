$mas_type2$ = <Noun>:<> ({<singular><direct>}:{} | {<singular><oblique>}:{e} |{<plural><direct>}:{e} | {<plural><oblique>}:{oM})
ALPHABET = [A-Za-z] [<Noun> a A e oM]:<> 
$delete-A$ = [e oM] <=> <> (<Noun>:<>[e oM]) 

"mas_type2.lex" $mas_type2$ || $delete-A$
