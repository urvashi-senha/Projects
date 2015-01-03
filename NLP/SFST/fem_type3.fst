$fem_type3$ = <Noun>:<> ({<singular><direct>}:{} | {<singular><oblique>}:{} |{<plural><direct>}:{eM} | {<plural><oblique>}:{oM} |  )
ALPHABET = [A-Za-z] [<Noun> A a eM oM]:<> 
$delete-A$ = [AeM AoM] <=> <> (<Noun>:<>[AeM oM]) 
"mas_type3.lex" $mas_type3$ 
