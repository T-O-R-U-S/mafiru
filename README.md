# Mafiru -- **MA**ss **FI**le **R**enaming **U**tility!
Initially made for a freelancing gig, I have now open-sourced this project.

## Usage:
`./mafiru.py (regular expression) (new file name).[f]`

## Example:
`./mafiru.py *.txt "text file[i][f]"`

## Custom parameters for new file name:
`[i]`: Current iteration (\[filename.txt, filenametwo.txt\] -> \[1, 2\])

`[e] or [f]`: File extension (filename.txt -> .txt)

`[n]`: Previous filename (filename.txt -> filename)
###### Suggest more custom parameters if you've got any ideas
