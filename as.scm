; racket -t as.scm
; (tl)
; (asv)
; http://localhost:8080
#lang racket/load

; is there a better way to prevent ac.scm from printing each
; statement?
(define default-print (current-print))
(current-print (lambda args #f))

(require "ac.scm") 
(require "brackets.scm")
(use-bracket-readtable)

(aload (aresolve "arc.arc"))
(aload (aresolve "libs.arc"))

(current-print default-print)

(tl)

