const MissionUtils = require("@woowacourse/mission-utils");

class App {
  constructor(){
    this._computer = [];
    this._player = [];
  }

  setting(){
    while(this._computer.length < 3){
        const NUMBER = MissionUtils.Random.pickNumberInRange(1, 9);
        if(!this._computer.includes(NUMBER))
            this._computer.push(NUMBER);
    }
  }

  play() {
    while(true){
      this.setting();
      console.log("숫자 야구 게임을 시작합니다.");
      
      let success = false;
      //let count = 0;
      while(!success){
        this.input();
        success = this.check();
        
      }

      if(this.end() == 2){
        break;
      }
    }
  }

  input(){
    MissionUtils.Console.readLine('숫자를 입력해주세요 : ', (PLAYER_NUMBER) => {
      const mapfn = (arg) => Number(arg);
      this._player = Array.from(PLAYER_NUMBER, mapfn)
    });

    if(this._player.length > 3)
      throw new Error("너무 많은 값을 입력했습니다. 게임을 종료합니다.");
    //else if(this._player.length < 3)
    //  throw new Error("너무 적은 값을 입력했습니다. 게임을 종료합니다.");
    this._player.forEach((num)=>{
      if(!(num >= 1 && num <= 9)){
          throw new Error("잘못된 값을 입력했습니다. 게임을 종료합니다.");
      }
    });
  }

  check(){
    console.log("[*] COMPUTER: "+ this._computer);
    console.log("[*] PLAYER: "+this._player);
    let strike = 0;
    let ball = 0;
    for(let i = 0; i<3 ; i++){
      const INDEX = this._player.indexOf(this._computer[i]);
      console.log("[*] INDEX: "+ INDEX);
      if(INDEX > -1){
        if(i === INDEX){
          strike += 1;
        }
        else{
          ball += 1;
        }
      }
      console.log("[*] STRIKE: " + strike + " BALL: "+ball);
    }
    //console.log("[*] strike: "+ strike + " / ball: "+ ball);
    if(strike == 0){
      if(ball == 0){
        console.log("낫싱");
      }
      else if(ball == 1){
        console.log("1볼");
      }
      else if(ball == 2){
        console.log("2볼");
      }
      else if(ball == 3){
        console.log("3볼");
      }
      else{
        console.log("[🚨] 채점에 문제가 생겼습니다.");
      }
    }

    else if(strike == 1){
      if(ball == 1){
        console.log("1스트라이크1볼");
      }
      else if(ball == 2){
        console.log("1스트라이크2볼");
      }
      else if(ball == 0){
        console.log("1스트라이크");
      }
      else{
        console.log("[🚨] 채점에 문제가 생겼습니다.");
      }
    }

    else if(strike == 2){
      if(ball == 0){
        console.log("2스트라이크");
      }
      else if(ball == 1){
        console.log("2스트라이크1볼");
      }
      else{
        console.log("[🚨] 채점에 문제가 생겼습니다.");
      }
    }

    else if(strike == 3){
      console.log("3스트라이크");
      console.log("3개의 숫자를 모두 맞히셨습니다! 게임 종료");
      return true;
    }

    return false;
  }

  end(){
    MissionUtils.Console.readLine('게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.\n', (answer) => {
        return answer;
    });
  }


}
module.exports = App;