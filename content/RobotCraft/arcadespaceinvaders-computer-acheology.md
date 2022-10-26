Title: Arcade/SpaceInvaders – Computer Acheology
Date: 2013-12-16 17:12
Author: Doug
Category: RobotCraft
Slug: arcadespaceinvaders-computer-acheology
Status: published

[Arcade/SpaceInvaders – Computer Acheology](http://www.computerarcheology.com/wiki/wiki/Arcade/SpaceInvaders)

Wow, this brings back memories! From the Z80 assembly language to the hardware specs. Those were the days.

```
09A5: 23              INC     HL                  ; Load ...
09A6: 7E              LD      A,(HL)              ; ... the ...
09A7: 23              INC     HL                  ; ... screen ...
09A8: 66              LD      H,(HL)              ; ... coordinates ...
09A9: 6F              LD      L,A                 ; ... to HL
09AA: C3 AD 09        JP      $09AD               ; ** Usually a good idea, but wasted here

;##-Print4Digits
; Print 4 digits in DE
09AD: 7A              LD      A,D                 ; Get first 2 digits of BCD or hex
09AE: CD B2 09        CALL    $09B2               ; Print them
09B1: 7B              LD      A,E                 ; Get second 2 digits of BCD or hex (fall into print)

;##-DrawHexByte
; Display 2 digits in A to screen at HL
09B2: D5              PUSH    DE                  ; Preserve
09B3: F5              PUSH    AF                  ; Save for later
```

More info at: [Arcade/SpaceInvaders – Computer Acheology](http://www.computerarcheology.com/wiki/wiki/Arcade/SpaceInvaders)
