if exists("b:current_syntax")
    finish
endif

let b:current_syntax = "truck"

syntax keyword truckKeyword use fn return
syntax keyword truckKeyword if else while
syntax keyword truckKeyword break continue
syntax keyword truckKeyword var
syntax keyword truckKeyword and or not
highlight link truckKeyword Keyword

syntax keyword truckFunction num str
syntax keyword truckFunction input print println
syntax keyword truckFunction type exit
highlight link truckFunction Function

syntax keyword truckBoolean true false
highlight link truckBoolean Identifier

syntax match truckOpreator "\v\<"
syntax match truckOpreator "\v\<="
syntax match truckOpreator "\v\>"
syntax match truckOpreator "\v\>="
syntax match truckOpreator "\v\=="
syntax match truckOpreator "\v\!="
syntax match truckOpreator "\v\="
syntax match truckOpreator "\v\!"
syntax match truckOpreator "\v\+"
syntax match truckOpreator "\v\-"
syntax match truckOpreator "\v\*"
syntax match truckOpreator "\v\/"
highlight link truckOperator Operator

syntax match truckString "\v\".*\""
syntax match truckString "\v\'.*\'"
highlight link truckString String

syntax match truckNumber "\v\d+"
highlight link truckNumber Number
