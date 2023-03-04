import re
txt = "I am doing nothing but we connect it"
'''Regular expressions (called REs, or regexes, or regex'
patterns) are essentially 
a tiny, highly specialized programming language embedded
inside Python and made available through the re module. Using this little
language, you specify the rules for the set of possible strings that you want to
match; this set might contain English sentences, or e-mail addresses, or TeX commands, or anything you like. You can then ask questions such as “Does this string match the pattern?”, or “Is there a match for the pattern anywhere in this string?”. You can also use REs to modify a string or to split it apart in various ways.

Regular expression patterns are compiled into a series of bytecodes which are then executed by a matching engine written in C. For advanced use, it may be necessary to pay careful attention to how the engine will execute a given RE, and write the RE in a certain way in order to produce bytecode that runs faster. Optimization isn’t covered in this document, because it requires that you have a good understanding of the matching engine’s internals.'''

#findall (return a list contaning all matches)
# search (return a match object if there is a match anywhere in the string )
# split (return a list where the string has been split at each string)
# sub  (replace one or many matches with a string)
# finditer (

patt = re.compiler(r'fass')
patt = re.compiler(r'lin$')
patt = re.compiler(r'aii*')
patt = re.compiler(r'.adm')
matches = patt.finditer(txt)
for match in matches:
    print(match) 
import re
txt = "fsdfv efbew ef ejf "

patt = re.compiler(r'[]adm')
patt = re.compiler(r'/adm')
patt = re.compiler(r'.adm')
patt = re.compiler(r'<adm')
patt = re.compiler(r'$adm')
patt = re.compiler(r'*adm')
patt = re.compiler(r'+adm')
patt = re.compiler(r'()adm')
patt = re.compiler(r'{}adm')
patt = re.compiler(r'?adm')
matches = patt.finditer(txt)
for match in matches:
    print(match)
    
    
    
    