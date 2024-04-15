GlowScript 3.1 VPython
##objects 

ball = sphere(pos=vector(-5,0,0), radius=0.5, color=color.cyan) 

wallRight = box(pos=vector(6,0,0), size=vector(0.2,12,12), color=color.green) 
wallLeft = box(pos=vector(-6,0,0), size=vector(0.2,12,12), color=color.green)
wallBack = box(pos=vector(0,0,-6), size=vector(12,12,0.2), color=color.green)
wallFront = box(pos=vector(0,0,6), size=vector(12,12,0.2), visible=False)
wallTop = box(pos=vector(0,6,0), size=vector(12,0.2,12), color=color.green)
wallBottom = box(pos=vector(0,-6,0), size=vector(12,0.2,12), color=color.green)

##initial values 

ball.velocity = vector(25,5,15)
deltat = 0.005 
t=0 
vscale = 0.1
varr = arrow(pos=ball.pos , axis=ball.velocity*vscale, color=color.yellow)
attach_trail(ball, color=ball.color)

##calculations 
scene.autoscale = 0

while t < 30:
  rate(100)
  if ball.pos.x > wallRight.pos.x - wallRight.size.x or ball.pos.x < wallLeft.pos.x + wallLeft.size.x:
    ball.velocity.x = -ball.velocity.x
    
  if ball.pos.y > wallTop.pos.y - wallTop.size.y or ball.pos.y < wallBottom.pos.y + wallBottom.size.y:
    ball.velocity.y = -ball.velocity.y
    
  if ball.pos.z > wallFront.pos.z - wallFront.size.z or ball.pos.z < wallBack.pos.z + wallBack.size.z:
    ball.velocity.z = -ball.velocity.z
    
  ball.pos = ball.pos + ball.velocity*deltat
  varr.pos = ball.pos
  varr.axis = ball.velocity*vscale
  t = t + deltat
  
