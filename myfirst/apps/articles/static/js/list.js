$(document).ready(function() {
    let images_heights = []
    let i = 0
    
    $('.device_image').each(function() {
        images_heights.push($(this).height())
    })

    $('.text').each(function() {
        $(this).height(
            images_heights[i] - $('.article_head').height()
        )
        i++
    })
    i = 0

    $('.content').each(function() {
        $(this).height(images_heights[i]);
        i++;
    })
});