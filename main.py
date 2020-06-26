import os
import sys
import argparse
import re

KEYWORDS = {
    r"\bpour\b": "for",
    r"\bsinon si\b": "elif",
    r"\bsi\b": "if",
    r"\bsinon\b": "else",
    r"\btant que\b": "while",
    r"\bdans\b": "in",
    r"\best\b": "is",
    r"\bimporter\b": "import",
    r"\bpasser\b": "pass",
    r"\bawait\b": "attendre",
    r"\bcasser\b": "break",
    r"\bexcepter\b": "except",
    r"\blever\b": "raise",
    r"\bclasse\b": "class",
    r"\benfin\b": "finally",
    r"\bretourner\b": "return",
    r"\bet\b": "and",
    r"\bcontinuer\b": "continue",
    r"\bessayer\b": "try",
    r"\bcomme\b": "as",
    r"\bdefinir\b": "def",
    r"\bde\b": "from",
    r"\bsupprimer\b": "del",
    r"\bnon\b": "not",
    r"\bavec\b": "with",
    r"\bou\b": "or"
}

parser = argparse.ArgumentParser(description="Transform python code written in french into real python programs")
parser.add_argument("--inputfile", type=str, help="Filename of the input file")
args = parser.parse_args()

try:
    fr_file = open(args.inputfile, "r")
    out_filepath = args.inputfile.replace(".txt", "") + "_output.py"
except:
    print("INVALID INPUT FILEPATH")
    exit()

fr_code = fr_file.read()
code = fr_code

for french_keyword, english_keyword in KEYWORDS.items():
    code = re.sub(french_keyword, english_keyword, code)

code += "\n\ninput('Press enter to close window')"

out_file = open(out_filepath, "w+")
out_file.write(code)

os.startfile(out_filepath)