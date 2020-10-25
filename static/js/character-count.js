    $('#content').keyup(function() {
        console.log('keyup function run')

    var characterCount = $(this).val().length,
      current = $('#current'),
      max = $('#maximum'),
      theCount = $('#the-count');

        limittext(characterCount, 1000)

    current.text(characterCount);


    /*This isn't entirely necessary, just playing around*/
        /*colours from: https://clrs.cc/ */
    if (characterCount < 100) {
    theCount.css('background', '#001f3f4D');
    }
    if (characterCount >= 100 && characterCount < 200) {
    theCount.css('background', '#0074D94D');
    }
    if (characterCount >= 200 && characterCount < 300) {
    theCount.css('background', '#7FDBFF4D');
    }
    if (characterCount >= 300 && characterCount < 400) {
    theCount.css('background', '#39CCCC4D');
    }
    if (characterCount >= 400 && characterCount < 500) {
    theCount.css('background', '#3D99704D');
    }
    if (characterCount >= 500 && characterCount < 600) {
    theCount.css('background', '#2ECC404D');
    }
    if (characterCount >= 600 && characterCount < 700) {
    theCount.css('background', '#01FF704D');
    }
    if (characterCount >= 700 && characterCount < 800) {
    theCount.css('background', '#FFDC004D');
    }
    if (characterCount >= 800 && characterCount < 900) {
    theCount.css('background', '#FF851B4D');
    }
    if (characterCount >= 900 && characterCount < 1000) {
    theCount.css('background', '#FF41364D');
    }

    if (characterCount >= 900) {
    maximum.css('background', '#FF41364D');
    current.css('background', '#FF41364D');
    theCount.css('font-weight','bold');
    } else {
    maximum.css('background','#001f3f4D');
    theCount.css('font-weight','normal');
    }


    });

    function limittext(charactercount, limit){
        content = document.getElementById('content')
        if (charactercount > limit)
        {content.value = content.value.substring(0, limit)}
    }