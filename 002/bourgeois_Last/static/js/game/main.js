var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');

canvas.width = window.innerWidth - 100;
canvas.height = window.innerHeight - 100;

// ctx.fillStyle = 'green'
// ctx.fillRect(10,10,100,100);

//이미지 그리기 (선인장)
//var img1 = new Image();
//img1.src = 'dino.jpeg';

//주인공
var dino = {
    x : 10,
    y : 200,
    width : 50,
    height : 50,
    draw(){ //그리는 함수
        ctx.fillStyle = 'green'
        ctx.fillRect(this.x, this.y, this.width, this.height);
        //ctx.drawImage(img1, this.x, this.y);
    }
}//dino

//이미지 그리기 (선인장)
//var img2 = new Image();
//img2.src = 'cactus.png'

//dino.draw() //그리기


//장애물
class Cactus{
    constructor(){
        this.x = 500;
        this.y = 200;
        this.width = 50;
        this.height = 50;
    }   
    draw(){ //그리는 함수
        ctx.fillStyle = 'red'
        ctx.fillRect(this.x, this.y, this.width, this.height);
        //ctx.drawImage(img2, this.x, this.y);
    }
}//Cactus

var cactus = new Cactus(); 
cactus.draw()


//1초에 60번 정도 ++1해줘야함
//프레임마다 1초에 움직이는 함수
//x축으로 이동
/*
function frame_per_act(){
    requestAnimationFrame(frame_per_act)

    ctx.clearRect(0,0,canvas.width, canvas.height);
    dino.x++; //1초마다 x좌표를 이동
    dino.draw() //그리기
}
frame_per_act();
*/

var timer = 0; //타이머
var cactus_list = []; //장애물 여러개 관리
var jump_timer =0; //점프타이머
// var random_speed = Math.floor(Math.random() * (7-1)+ 1);
var animation;

//내가 이동하는게 아니라 장애물이 다가오게
function frame_per_act(){
    animation = requestAnimationFrame(frame_per_act)
    timer++;
    ctx.clearRect(0,0,canvas.width, canvas.height);
    var random_speed = Math.floor(Math.random() * (7-1)+ 1);
    
    if(timer%60 ===0 ){
        var cactus = new Cactus(); 
        cactus_list.push(cactus)
        
    }
    cactus_list.forEach((a, i, o)=>{
        //x좌표가 0미만이면 제거
        if(a.x < 0){
            o.splice(i,1)
        }

        //a.x-=3;
        a.x-=random_speed; //랜덤 스피드로 오게끔
        
        is_it_collision(dino,a);

        a.draw();
    })
    if(jump_action==true){ //점프중일때

        dino.y-=3; //점프 속도
        jump_timer++;
    }
    if(jump_action==false){ //점프중이 아닐때
        if(dino.y < 200){
            dino.y+=3;  //점프 속도
        }
    }
    if(jump_timer >50){ //100프레임 시간이 지나면 점프 중단
        jump_action = false;
        jump_timer = 0;
    }
    dino.draw()

}//frame_per_act
frame_per_act();

//충돌 확인
function is_it_collision(dino,cactus){
    var x_distance = cactus.x - (dino.x + dino.width);
    var y_distance = cactus.y - (dino.y + dino.height);
    if(x_distance<0 && y_distance<0){
        ctx.clearRect(0,0,canvas.width, canvas.height); //캔버스 클리어
        cancelAnimationFrame(animation); //게임 중단 
        alert('Game Over')
        
    }
}

var jump_action = false;
document.addEventListener('keydown', function(e){
    if(e.code === 'Space'){
        jump_action = true;
    }
})//addEventListener





