$(document).ready(function() {
    countdown.setLabels(
        ' milliseconde| seconde| minute| heure| jour| semaine| mois| année| décennie| siècle| millénaire',
        ' millisecondes| secondes| minutes| heures| jours| semaines| mois| années| décennies| siècles| millénaires',
        ' et ', ', ', 'maintenant'
    );
    function timer() {
        $('.artwork_timer').each(function() {
            var timeleft = moment().countdown($(this).val())
            if(moment().isBefore(moment($(this).val()))) {
                $(this).next('.timer').html(timeleft.toString())
            }
        });
    }
    timer();
    setInterval(timer, 1000);
}); 
