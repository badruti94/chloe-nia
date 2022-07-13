
style word_list is button:
    background "#ECB390"              # Yellow 
style word_list_text is text:
    size 35
    hover_color "#CA4E79"             # Pink
    color "#ffffff"                   # Red


screen SelectKeyword():
    frame:
        xalign 0.5
        yalign 0.5
        background '#ECB390'
        xpadding 25
        ypadding 25
        vbox:
            spacing 5
            hbox:
                spacing 25
                textbutton 'Anime' style 'word_list':
                    action [SetVariable('niaPoin', niaPoin + 1), Return()]
                textbutton 'Vocaloid' style 'word_list':
                    action [SetVariable('niaPoin', niaPoin + 1), Return()]
                textbutton 'Taruh' style 'word_list':
                    action [SetVariable('chloePoin', chloePoin + 1), Return()]
                textbutton 'Game' style 'word_list':
                    action [SetVariable('niaPoin', niaPoin + 1), Return()]
            hbox:
                spacing 25
                textbutton 'Luffy' style 'word_list':
                    action [SetVariable('niaPoin', niaPoin + 1), Return()]
                textbutton 'Bertaut' style 'word_list':
                    action [SetVariable('chloePoin', chloePoin + 1), Return()]
                textbutton 'Lagu:' style 'word_list':
                    action [SetVariable('chloePoin', chloePoin + 1), Return()]
                textbutton 'Yoasobi' style 'word_list':
                    action [SetVariable('niaPoin', niaPoin + 1), Return()]
            hbox:
                spacing 25
                textbutton 'Waifu' style 'word_list':
                    action [SetVariable('niaPoin', niaPoin + 1), Return()]
                textbutton 'Nolep' style 'word_list':
                    action [SetVariable('niaPoin', niaPoin + 1), Return()]
                textbutton 'Peterpan' style 'word_list':
                    action [SetVariable('chloePoin', chloePoin + 1), Return()]
                textbutton 'Indie' style 'word_list':
                    action [SetVariable('chloePoin', chloePoin + 1), Return()]
            hbox:
                spacing 25
                textbutton 'Dewasa' style 'word_list':
                    action [SetVariable('chloePoin', chloePoin + 1), Return()]
                textbutton 'Semanggi' style 'word_list':
                    action [SetVariable('chloePoin', chloePoin + 1), Return()]
                textbutton 'Orange' style 'word_list':
                    action [SetVariable('niaPoin', niaPoin + 1), Return()]
                textbutton 'Senja' style 'word_list':
                    action [SetVariable('chloePoin', chloePoin + 1), Return()]
