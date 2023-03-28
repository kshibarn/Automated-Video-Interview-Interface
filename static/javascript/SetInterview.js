const addQuestion = document.querySelector("[data-addQuestion]");
const newQuestionInput = document.querySelector("[data-newQuestionInput]");
const timeLimitInput = document.querySelector("[data-timeLimitInput]");
const questionTemplate = document.querySelector("[data-questionTemplate]");
const popupAddingContainer = document.querySelector(".popup-adding-container");
const addSubmitBtn = document.querySelector("[data-add-submit-btn]")
const popupForm = document.querySelector(".popup-form");
const interviewName = document.querySelector("input[name=interviewName]");
const companyName = document.querySelector("input[name=companyName]");
const lastDate = document.querySelector("input[name=lastDate]");

addQuestion.addEventListener('click' , () =>{
    popupAddingContainer.classList.add("active");
})

addSubmitBtn.addEventListener('click' ,() =>{
    popupAddingContainer.classList.remove("active");
})

popupForm.addEventListener('submit', (event) => {
	event.preventDefault();

    let newQues = document.createElement('div');
    newQues.textContent=newQuestionInput.value;

    let timeLimit = document.createElement('div');
    timeLimit.textContent=timeLimitInput.value + ' min';

    let questionBox = document.createElement('li');
    questionBox.classList.add("question-box")
    questionBox.appendChild(newQues);
    questionBox.appendChild(timeLimit);
    

    questionTemplate.appendChild(questionBox);

    newQuestionInput.value='';
    timeLimitInput.value='';
});