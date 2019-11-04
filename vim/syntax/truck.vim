if exists("b:current_syntax")
    finish
endif

let b:current_syntax = "truck"

syntax keyword truckKeyword and break class continue
syntax keyword truckKeyword else extends function if
syntax keyword truckKeyword let or not return use
syntax keyword truckKeyword while
highlight link truckKeyword Keyword

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
syntax match truckOpreator "\v\%"
syntax match truckOpreator "\v\&"
syntax match truckOpreator "\v\|"
syntax match truckOpreator "\v\^"
highlight link truckOperator Operator

syntax region truckString start=/\v"/ skip=/\v\\./ end=/\v"/
highlight link truckString String

syntax match truckNumber "\v\d+"
highlight link truckNumber Number

syntax match truckComment "\v#.*$"
highlight link truckComment Comment

