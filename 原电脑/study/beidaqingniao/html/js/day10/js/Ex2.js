for(let cock=1; cock<15; cock++) {
        for (let hen = 1; hen < (100-cock*5)/3; hen++) {
            let biddy=100-cock-hen;
            if (biddy/3 + hen*3 + cock*5 == 100){
                console.log("公鸡是: ", cock, "母鸡是: ", hen, "小鸡是: ", biddy);
        }
    }
}