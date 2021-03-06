
define e = Character('Eileen', color="#c8ffc8")
define chloe  = Character('Chloe', color='#ff0000')
define nia  = Character('Nia', color='#0000ff')
define n  = Character('[name]', color='#00ff00')

default chloePoin = 0
default niaPoin = 0


# Game dimulai disini.
label start:
    scene bg kelas with dissolve

    'Disclaimer : Seluruh asset di VN ini bukan milik saya. \n Game berbentuk VN ini merupakan sebuah fanmade. VN ini tidak untuk penggunaan komersil. Hanya untuk seru - seruan saja.'
    $ name = renpy.input('Siapa namamu?')
    $ name = name.strip()
    play music 'audio/bgm/Yummy Flavor.mp3' fadein 1.0 volume 0.5
    'Suatu pagi di sebuah kelas. Ada 3 remaja sedang mengerjakan tugas sekolah bahasa Indonesia. Ada Nia, Chloe, dan [name]. '
    'Chloe adalah seorang gadis penyuka senja. Dia suka sekali mendengarkan lagu - lagu indie yang bertemakan kedewasaan. Sementara Nia adalah seorang gadis wibu nolep yang sangat suka marathon anime.'
    show chloe
    chloe 'Mmmm... masih ada kata - kata yang kurang. Kamu ada tambahan ga Nia?'
    show chloe at left with easeinleft
    show nia at right with dissolve
    nia 'Aku ga ada'
    chloe 'Kalo kamu [name]?'
    n 'Ada. Sedikit'

    'Klik/Sentuh salah satu dari pilihan kata berikut'
    call screen SelectKeyword()

    chloe 'Besok kita jalan yuk ke kota tua'
    n 'Wah boleh tuh'
    chloe 'Kamu gimana Nia?'
    nia 'Aku sih ikut aja'
    chloe 'Oke. Besok jadi ya.'
    n 'Mau ketemuan dimana?'
    chloe 'Kita langsung ke tempatnya aja gimana? Eh tapi kamu belum tau tempatnya ya. Nia kamu bisa samperin [name] ga?'

    if(chloePoin > niaPoin):
        jump chloe_route
    else:
        jump nia_route

label pulang_sekolah:
    play sound 'audio/sfx/bel masuk sekolah.mp3' fadein 1.0 volume 0.5
    'Bell sekolah pun sudah berbunyi tanda waktu untuk pulang'

    hide chloe
    hide nia
    stop sound fadeout 1.0

    return

# rute chloe
label chloe_route:
    nia 'aku ... ga bisa'
    chloe 'Oh ya udah aku aja. Aku samperin jam 8 ya'

    call pulang_sekolah from _call_pulang_sekolah


    scene bg rumah
    show chloe

    chloe 'Udah siap?'
    n 'Udah nih'
    chloe 'Okeh'

    scene bg jalanan
    show chloe
    stop music fadeout 1.0
    play music 'audio/bgm/A Quiet Thought.mp3' fadein 1.0 volume 0.5
    chloe 'Nee [name]. Ku dengar kamu suka lagu indie juga.'
    n 'Dikit sih.'
    chloe 'Mmm... Suka lagu siapa aja'
    n  'Aku suka lagu Nadin Amizah yang taruh'
    chloe 'Aku kira kamu ga suka lagu cinta - cintaan'
    n 'Entah kenapa aku merasa itu bukan tentang cinta tapi tentang kehidupan'
    chloe 'Selain itu apa lagi?'
    n 'Mmmm apa ya? Untuk saat ini sih baru sekitar lagu Nadin Amizah saja'

    jump jalan_jalan

# rute nia
label nia_route:
    nia 'bisa sih ...'
    chloe 'Oke. Kamu samperin jam 8 ya'

    call pulang_sekolah from _call_pulang_sekolah_1


    scene bg rumah
    show nia

    nia 'Udah siap?'
    n 'Udah nih'
    nia 'Okeh'

    scene bg jalanan
    show nia
    stop music fadeout 1.0
    play music 'audio/bgm/A Quiet Thought.mp3' fadein 1.0 volume 0.5
    nia 'Ano... '
    n 'Apa?'
    nia 'Aku pernah liat di HPmu kamu browsing gambar anime. Eh maaf aku tidak bermaksud untuk mengintip HPmu'
    nia 'Ada yang mau aku tanyakan. Apa kamu suka anime juga?'
    n 'Oh itu. Iya. Dulu aku suka anime tapi sekarang sudah tidak'
    nia 'Eh kenapa?'
    n 'Sekarang aku mau fokus dulu ke pendidikanku'
    nia 'Eh tapi ... begitu ya. Baiklah'

    jump jalan_jalan

# jalan - jalan
label jalan_jalan:
    scene bg kota
    show chloe

    chloe 'Kalian ga beli? Masa cuma liat - liat doang sih?'
    n 'Barang - barangnya terlalu  mahal. Selain itu aku lagi hemat uang'

    show chloe at left with easeinleft
    show nia at right with dissolve
    nia 'Betul betul. Aku juga begitu'
    chloe 'Jangan begitu. Kita memang tidak boleh boros tapi nggak apa - apa sesekali membeli barang yang disuka. '
    chloe 'Benda seperti ini memang terlihat tidak ada fungsinya tapi benda seperti ini ibarat perangkat penyimpanan komputer bisa menjadi penyimpan memori. Kamu akan mengingat sesuatu jika melihat benda - benda ini'
    '[name] membeli sesuatu untuk dirinya dan satunya lagi untuk seseorang'

    # if
    if(chloePoin > niaPoin):
        # rute chloe
        n 'Chloe. Ini untukmu.'
        chloe 'Terima kasih ya.'
        n 'Ku pikir benda ini cocok untukmu. Kamu kan suka sekali dengan musik jadi aku belikan gantungan kunci bentuk gitar'
    else:
        # rute chloe
        n 'Nia. Ini untukmu.'
        nia 'Eh. Mmm... Terima kasih'
        n 'Ku pikir benda ini cocok untukmu. Kamu kan suka anime one piece jadi aku belikan gantungan kunci bentuk luffy'

    jump end

label end:
    hide chloe
    hide nia with dissolve
    'Mereka pun pulang ...'

    call credits from _call_credits
    return

