$(document).ready(function () {
    var controller = new ScrollMagic.Controller()

    var second = new ScrollMagic.Scene({
            triggerElement: '#second',
            duration: "100%",
        })
        .setClassToggle('body', 'red-bg')
        .addTo(controller);

    var third = new ScrollMagic.Scene({
            triggerElement: '#third',
            duration: "100%",
        })
        .setClassToggle('body', 'green-bg')
        .addTo(controller);

    var fourth = new ScrollMagic.Scene({
            triggerElement: '#fourth',
            duration: "100%",
        })
        .setClassToggle('body', 'blue-bg')
        .addTo(controller);
})