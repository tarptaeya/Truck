if exists("b:current_syntax")
    finish
endif

let b:current_syntax = "truck"

syntax keyword truckKeyword fn print return
syntax keyword truckKeyword if else while
syntax keyword truckKeyword break continue
syntax keyword truckKeyword var
highlight link truckKeyword Keyword

syntax keyword truckBoolean true false
highlight link truckBoolean Boolean

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
