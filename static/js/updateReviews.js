editButtons = document.querySelectorAll(".edit-product-review");

for (const button of editButtons) {
  button.addEventListener("click", () => {
    // first ask the user what they want the new review to be
    const newComment = prompt("What is your new Comment for this movie?");
    const formInputs = {
      updated_Comment: newComment,
      review_id: button.id,
    };

    // send a fetch request to the update_review route
    fetch("/update_review", {
      method: "POST",
      body: JSON.stringify(formInputs),
      headers: {
        "Content-Type": "application/json",
      },
    }).then((response) => {
      if (response.ok) {
        document.querySelector(`span.review_num_${button.id}`).innerHTML =
          newComment;
      } else {
        alert("Failed to update review.");
      }
    });
  });
}
