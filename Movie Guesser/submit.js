//submit button for end of page

let submitButton = document.getElementById('submit')

    submitButton.addEventListener('click', function() {

        let choice = document.getElementById('choice').value

        if (choice == 'Ponyo') {

                alert('Correct!')

        } 

        else {

            alert('Incorrect!')

        }

    })