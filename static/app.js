
const up_vote_spans = document.getElementsByClassName("up-vote");
const down_vote_spans = document.getElementsByClassName("down-vote");
const count = document.getElementsByClassName("number");
let votes = [];
for (let i = 0; i < count.length; i += 1) {
    const thisUpVoteSpan = up_vote_spans[i];
    const thisDownVoteSpan = down_vote_spans[i];
    if (up_vote_spans[i].style.color == "rgb(60, 188, 141)") {
        votes[i] = {
            up: true,
            down: false
        };
    } else if (down_vote_spans[i].style.color == "rgb(60, 188, 141)") {
        votes[i] = {
            up: false,
            down: true
        };
    } else {
        votes[i] = {
            up: false,
            down: false
        };
    }
    thisUpVoteSpan.addEventListener("click", handleUpvote.bind( this,i), false);
    thisDownVoteSpan.addEventListener("click", handleDownvote.bind( this,i), false);
}

function handleUpvote(i,e) {
    
    
    const currentVote = votes[i];
    const matchingUpSpan = up_vote_spans[i];
    const matchingDownSpan = down_vote_spans[i];
    const matchingCount = count[i];
    const currentCount = parseInt(matchingCount.innerHTML);
    if (i != 0) {
        type = "answer";
    } else {
        type = "ques";
    }
    var ifvote = "novote";
    if (e.target.id != $("#global_session_user").val()){
    if (currentVote.down) {
        matchingCount.innerHTML = currentCount + 2;
    } else if (currentVote.up === false) {
        matchingCount.innerHTML = currentCount + 1;
    } else {
        matchingCount.innerHTML = currentCount - 1;
    }
    if (!currentVote.up) {
        console.log(currentVote.up, currentVote.down);
        matchingUpSpan.style.color = "#3CBC8D";
        matchingDownSpan.style.color = "dimgray";
        currentVote.up = true;
        currentVote.down = false;
        ifvote = "upvote";
    } else {
        matchingUpSpan.style.color = "dimgray";
        currentVote.up = false;
    }
    }
    else{
        $("#show_popups").append(`<div class="alert alert-warning alert-dismissible fade show" role="alert" style="position:fixed; left: 50%; transform: translate(-50%, 0);">
  You can't vote your own answer or question.🙂
  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
</div>`)
    }
    $.ajax({
        type: "GET",
        url: `${window.location.pathname}`,
        data: {
            vote: matchingCount.innerHTML,
            votetype: ifvote,
            ques_no: matchingCount.id.split("_")[1],
            type: type,
            voteuser:e.target.id 
        },
        contentType: "application/json;charset=UTF-8",
        success: function(response) {
            if (response == "login") {
                document.location.replace("/signin")
            }
            if (response == "sameuser"){
                
                matchingUpSpan.style.color = "dimgray";
                currentVote.up = false;
                console.log("hi")
            }
        },
    });
}

function handleDownvote(i,e) {
    
    const currentVote = votes[i];
    const matchingUpSpan = up_vote_spans[i];
    const matchingDownSpan = down_vote_spans[i];
    const matchingCount = count[i];
    const currentCount = parseInt(matchingCount.innerHTML);
    if (i != 0) {
        type = "answer";
    } else {
        type = "ques";
    }
    var ifvote = "novote";
    if (e.target.id != $("#global_session_user").val()){

    
    if (currentVote.up) {
        matchingCount.innerHTML = currentCount - 2;
    } else if (currentVote.down === false) {
        matchingCount.innerHTML = currentCount - 1;
    } else {
        matchingCount.innerHTML = currentCount + 1;
    }
    if (!currentVote.down) {
        matchingDownSpan.style.color = "#3CBC8D";
        matchingUpSpan.style.color = "dimgray";
        currentVote.down = true;
        currentVote.up = false;
        ifvote = "downvote";
    } else {
        matchingDownSpan.style.color = "dimgray";
        currentVote.down = false;
    }
    }
    else{
         $("#show_popups").append(`<div class="alert alert-warning alert-dismissible fade show" role="alert" style="position:fixed; left: 50%; transform: translate(-50%, 0);">
  You can't vote your own answer or question.🙂
  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
</div>`)

    }
    $.ajax({
        type: "GET",
        url: `${window.location.pathname}`,
        data: {
            vote: matchingCount.innerHTML,
            votetype: ifvote,
            ques_no: matchingCount.id.split("_")[1],
            type: type,
            voteuser:e.target.id
        },
        contentType: "application/json;charset=UTF-8",
        success: function(res) {
            console.log(res);
            if (res == "sameuser"){
                

                matchingDownSpan.style.color = "dimgray";
                currentVote.down = false;
            }
        },
    });
}
var no_check = false
for (i = 0; i < $(".svg-icon").length; i++) {
    if ($(".svg-icon").eq(i).attr("fill") == "#48a868") {
        no_check = true
    }
}

if (no_check) {
    $('.svg-icon').filter(function() {
        return $(this).attr("fill") == "#bbc0c4";
    }).hide();
}

// correct answer
$(".svg-icon").click(function(e) {
    var real = false
    if ($(this).attr("fill") == "#bbc0c4") {
        $(this).attr("fill", "#48a868");
        real = true
        $('.svg-icon').filter(function() {
            return this.id != e.currentTarget.id;
        }).hide();
    } else {
        $(this).attr("fill", "#bbc0c4");
        real = false
        $('.svg-icon').filter(function() {
            return this.id != e.currentTarget.id;
        }).show();
    }
    $.ajax({
        type: "GET",
        url: `${window.location.pathname}`,
        data: {
            real_answer: real,
            number: this.id
        },
        contentType: "application/json;charset=UTF-8",
        success: function(response) {
            if (response == "login") {
                document.location.replace("/signin")
            }
        },
    });
});



    // $.ajax({
    //     type: "GET",
    //     url: `${window.location.pathname}`,
    //     data: {
    //         real_answer: real,
    //         number: this.id
    //     },
    //     contentType: "application/json;charset=UTF-8",
    //     success: function(response) {
    //         if (response == "login") {
    //             document.location.replace("/signin")
    //         }
    //     },
    // });




console.log( window.innerWidth  - $(".container").css("margin-left").replace(/[^-\d\.]/g, '') )
$(".mce-content-body").css({

    "width": window.innerWidth  -( $(".container").css("margin-right").replace(/[^-\d\.]/g, '') *2 +60  )
  })
$(window).resize(function() {
    $(".mce-content-body").css({
        "width": window.innerWidth  - ( $(".container").css("margin-right").replace(/[^-\d\.]/g, '')*2 +60) 
    })
})


