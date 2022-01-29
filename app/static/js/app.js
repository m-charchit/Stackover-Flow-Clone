const up_vote_spans = document.getElementsByClassName("up-vote");
const down_vote_spans = document.getElementsByClassName("down-vote");
const count = document.getElementsByClassName("number");
const svg = document.querySelectorAll(".svg-icon")

let votes = [];


const handleUpvote = async (i, e) => {
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
    if (e.target.id != document.getElementById("global_session_user").value) {
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
    } else {
        document.getElementById("show_popups").innerHTML = `<div class="alert alert-warning alert-dismissible fade show" role="alert" style="position:fixed; width:85%; left: 50%; transform: translate(-50%, 0);">
  You can't vote your own answer or question.
  <button type="button" class="btn-close" data-mdb-dismiss="alert" aria-label="Close"></button>
</div>`
    }
    const request = await fetch('/cast_vote', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            votetype: ifvote,
            ques_no: matchingCount.id.split("_")[1],
            type: type,
            voteuser: e.target.id,
        }),
    })
    response = await request.text()
    if (response == "sameuser") {
        matchingUpSpan.style.color = "dimgray";
        currentVote.up = false;
        console.log("hi");
    } else if (response == "login") {
        document.location.replace("/signin");
    }
}

const handleDownvote = async (i, e) => {
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
    if (e.target.id != document.getElementById("global_session_user").value) {
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
    } else {
        document.getElementById("show_popups").innerHTML = `<div class="alert alert-warning alert-dismissible fade show" role="alert" 
        style="position:fixed; width:85%; left: 50%; transform: translate(-50%, 0);">
  You can't vote your own answer or question.
  <button type="button" class="btn-close" data-mdb-dismiss="alert" aria-label="Close"></button>
</div>`
    }
    const request = await fetch('/cast_vote', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            votetype: ifvote,
            ques_no: matchingCount.id.split("_")[1],
            type: type,
            voteuser: e.target.id,
        }),
    })
    response = await request.text();
    if (response == "sameuser") {
        matchingUpSpan.style.color = "dimgray";
        currentVote.up = false;
        console.log("hi");
    } else if (response == "login") {
        document.location.replace("/signin");
    }

}

for (let i = 0; i < count.length; i += 1) {
    const thisUpVoteSpan = up_vote_spans[i];
    const thisDownVoteSpan = down_vote_spans[i];
    if (up_vote_spans[i].style.color == "rgb(60, 188, 141)") {
        votes[i] = {
            up: true,
            down: false,
        };
    } else if (down_vote_spans[i].style.color == "rgb(60, 188, 141)") {
        votes[i] = {
            up: false,
            down: true,
        };
    } else {
        votes[i] = {
            up: false,
            down: false,
        };
    }
    thisUpVoteSpan.addEventListener("click", handleUpvote.bind(this, i), false);
    thisDownVoteSpan.addEventListener(
        "click",
        handleDownvote.bind(this, i),
        false
    );
}

var no_check = false;
for (i = 0; i < svg.length; i++) {
    if (svg[i].getAttribute("fill") == "#48a868") {
        no_check = true;
    }
}

if (no_check) {
    let filteredSvg = [...svg].filter(e => {
        return e.getAttribute("fill") == "#bbc0c4";
    })
    for (i of filteredSvg) {
        i.classList.add("d-none")
    }

}
console.log(svg)
// correct answer
svg.length != 0 && svg.forEach(element => {
    element.addEventListener("click", async (e) => {
        console.log(this)
        let real = false;
        if (e.target.getAttribute("fill") == "#bbc0c4") {
            e.target.setAttribute("fill", "#48a868");
            real = true;
            let filteredSvg = [...svg].filter(elem => {

                return e.target.id != elem.id;
            })
            for (i of filteredSvg) {
                i.classList.add("d-none")
            }

        } else {
            e.target.setAttribute("fill", "#bbc0c4");
            real = false;
            let filteredSvg = [...svg].filter(elem => {
                return e.target.id != elem.id;
            })
            for (i of filteredSvg) {
                i.classList.remove("d-none")
            }
        }
        let ansId = e.target.classList.length == 0 ? e.target.parentElement.id : e.target.id
        console.log(ansId)
        const request = await fetch(`${window.location.pathname}?real_answer=${real}&number=${ansId}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json;charset=UTF-8',
            },
        })
        response = await request.text();

    }, false);
});
const textArea = document.querySelectorAll(".textarea")
textArea.length != 0 && textArea.forEach(element => {
    element.addEventListener("input", function (e) {
        e.target.previousElementSibling.value = tinyMCE.activeEditor.getContent();
    });
});


function resizeContent() {
    let mceContent = document.querySelectorAll(".mce-content-body")
    mceContent.length != 0 && mceContent.forEach(e => {
        e.style.width = window.innerWidth - document.getElementsByClassName("container")[0].style.marginRight.replace(/[^-\d\.]/g, "") * 2 + 60
    })

}
resizeContent()
window.addEventListener("resize", (e) => {
    resizeContent()
})