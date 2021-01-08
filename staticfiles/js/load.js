// console.log('hello word')
// $(document).ready(function() {
//     $(".load-btn").on('click', function() {
//         var _loadb = $(".row").length;
//         //run ajax
//         $.ajax({
//             url: "{% url 'load' %}",
//             type: "post",
//             data: {
//                 'offset': _loadb,
//                 'csrfmiddlewaretoken': "{{csrf_token}}"
//             },
//             dataType: 'json',
//             // dataType2: 'jason2',
//             beforeSend: function() {
//                 $(".load-btn").addClass('disabled').text('Loading..');

//             },
//             success: function(res) {
//                 console.log(res)
//             },
//         });
//     });
// });