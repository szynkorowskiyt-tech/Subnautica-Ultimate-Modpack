const data = {

    lang: "Polish",


    Polish: {


        quest_1: {

            name: "Początek przygody!",

            description:
            "Zrób skaner",

            rarity: "Common",

            requires: []

        },


        quest_2: {

            name: "Wytwórz niezbędne narzędzia nurka!",

            description:
            "Wytwórz Nóż survivalowy, Standardową butle O2, Płetwy",

            rarity: "Common",

            requires: [
                "quest_1"
            ]

        },


        quest_3: {

            name: "Spragniony?",

            description:
            "Wytwórz 4 butelki wody (350ml), 2 konserwowane rybki",

            rarity: "Common",

            requires: [
                "quest_1"
            ]

        },


        quest_4: {

            name: "Król potworów",

            description:
            "Pokonaj najpotężniejszego przeciwnika w całej krainie.",

            rarity: "Legendary",

            requires: [
                "quest_3"
            ]

        }


        /*
        
        quest_5: {

            name: "Nowy quest",

            description:
            "Opis nowego questa.",

            rarity: "Common",

            requires: [
                "quest_4"
            ]

        }

        */


    },





    English: {


        quest_1: {

            name: "First Step",

            description:
            "Defeat 10 enemies and start your adventure.",

            rarity: "Common",

            requires: []

        },


        quest_2: {

            name: "Lost Treasure",

            description:
            "Find the hidden chest deep inside the forest.",

            rarity: "Rare",

            requires: [
                "quest_1"
            ]

        },


        quest_3: {

            name: "Ancient Ruins",

            description:
            "Discover ancient ruins and their secrets.",

            rarity: "Epic",

            requires: [
                "quest_2"
            ]

        },


        quest_4: {

            name: "Monster King",

            description:
            "Defeat the strongest enemy in the kingdom.",

            rarity: "Legendary",

            requires: [
                "quest_3"
            ]

        }


    }

};





let lang = data.lang;



let completed =
JSON.parse(
    localStorage.getItem("quests")
)
|| [];






document
.getElementById("language")
.value = lang;






document
.getElementById("language")
.onchange = e => {

    lang = e.target.value;

    render();

};









function render(){


    let box =
    document.getElementById("quests");


    box.innerHTML = "";



    let quests =
    data[lang];



    let done = 0;





    Object.keys(quests)
    .forEach(id => {


        let q = quests[id];



        let unlocked =
        q.requires.every(
            x => completed.includes(x)
        );



        if(completed.includes(id)){

            done++;

        }





        let card =
        document.createElement("div");



        card.className =
        "card " + q.rarity;





        if(!unlocked){

            card.classList.add("locked");

        }




        if(completed.includes(id)){

            card.classList.add("completed");

        }






        card.innerHTML = `


        <h2>

        ${completed.includes(id) ? "✅" : "🟢"}

        ${q.name}

        </h2>



        <p>

        ${q.description}

        </p>



        <p>

        ⭐ ${q.rarity}

        </p>




        <p>

        ${
            !unlocked
            ?
            "🔒 Locked"

            :

            completed.includes(id)
            ?

            "✅ Completed"

            :

            "🟢 Available"

        }

        </p>





        ${
            unlocked && !completed.includes(id)

            ?

            `

            <button onclick="completeQuest('${id}')">

            ✔ Complete

            </button>

            `

            :

            ""

        }



        `;





        box.appendChild(card);



    });






    let total =
    Object.keys(quests).length;



    let percent =
    (done / total) * 100;





    document
    .getElementById("bar")
    .style.width =
    percent + "%";






    document
    .getElementById("stats")
    .innerHTML =

    `${done}/${total} (${Math.round(percent)}%)`;



}









function completeQuest(id){


    completed.push(id);


    save();


    render();


}










function resetQuests(){


    if(!confirm(
        "Na pewno?"
    ))

    return;




    if(!confirm(
        "NAPEWNO? Cały postęp zostanie usunięty!"
    ))

    return;





    completed = [];



    save();



    render();



}










function save(){


    localStorage.setItem(

        "quests",

        JSON.stringify(completed)

    );


}










render();