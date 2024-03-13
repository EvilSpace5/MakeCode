controller.combos.attachCombo("ua", function on_combos_attach_combo() {
    
    projectile = sprites.createProjectileFromSprite(img`
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 1 1 3 . . . . . . 
                    . . . . . . 1 3 . 3 3 . . . . . 
                    . . . . . . 1 . . . 3 2 2 3 . . 
                    . . . . . 1 3 . . . 2 2 1 3 3 . 
                    . . . . . 1 3 . 2 2 3 1 1 1 3 . 
                    . . 2 2 2 1 3 3 3 3 3 1 1 1 3 . 
                    . . 1 1 1 1 3 1 1 1 1 1 1 1 3 . 
                    . . 2 2 2 1 3 3 3 3 3 1 1 1 3 . 
                    . . . . . 1 3 . 2 2 3 1 1 1 3 . 
                    . . . . . 1 3 . . . 2 2 1 3 3 . 
                    . . . . . . 1 . . . 3 2 2 3 . . 
                    . . . . . . 1 3 . 3 3 . . . . . 
                    . . . . . . . 1 1 3 . . . . . . 
                    . . . . . . . . . . . . . . . .
        `, MeBoi, 50, 1)
    projectile.setScale(1.25, ScaleAnchor.Middle)
})
statusbars.onZero(StatusBarKind.Health, function on_on_zero(status2: StatusBarSprite) {
    game.gameOver(false)
    game.splash("YOU LOSE")
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap(sprite2: Sprite, otherSprite2: Sprite) {
    MeBoiHealth.value += -1
})
statusbars.onZero(StatusBarKind.EnemyHealth, function on_on_zero2(status: StatusBarSprite) {
    game.gameOver(true)
    game.splash("YOU WIN")
})
controller.combos.attachCombo("uuddlrlrab", function on_combos_attach_combo2() {
    MeBoiHealth.value = 500
    MeBoiHealth.max += 500
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function on_on_overlap2(sprite: Sprite, otherSprite: Sprite) {
    MisterBadGuyHealth.value += -1
})
let projectile : Sprite = null
let MisterBadGuyHealth : StatusBarSprite = null
let MeBoiHealth : StatusBarSprite = null
let MeBoi : Sprite = null
scene.setBackgroundColor(14)
music.play(music.stringPlayable("B A G A G F A C5 ", 120), music.PlaybackMode.UntilDone)
controller.combos.setExtendedComboMode(true)
MeBoi = sprites.create(img`
        ........................
            .....ffff...............
            ...fff22fff.............
            ..fff2222fff............
            .fffeeeeeefff...........
            .ffe222222eef...........
            .fe2ffffff2ef...........
            .ffffeeeeffff...........
            ffefbf44fbfeff..........
            fee41fddf14eef..........
            .ffffdddddeef...........
            fddddf444eef............
            fbbbbf2222f4e...........
            fbbbbf2222fd4...........
            .fccf45544f44...........
            ..ffffffff..............
            ....ff..ff..............
            ........................
            ........................
            ........................
            ........................
            ........................
            ........................
            ........................
    `, SpriteKind.Player)
let Mister_Bad_Guy = sprites.create(img`
        . . . . . . . . . b 5 b . . . . 
            . . . . . . . . . b 5 b . . . . 
            . . . . . . b b b b b b . . . . 
            . . . . . b b 5 5 5 5 5 b . . . 
            . . . . b b 5 b c 5 5 d 4 c . . 
            . b b b b 5 5 5 b f d d 4 4 4 b 
            . b d 5 b 5 5 b c b 4 4 4 4 b . 
            . . b 5 5 b 5 5 5 4 4 4 4 b . . 
            . . b d 5 5 b 5 5 5 5 5 5 b . . 
            . b d b 5 5 5 d 5 5 5 5 5 5 b . 
            b d d c d 5 5 b 5 5 5 5 5 5 b . 
            c d d d c c b 5 5 5 5 5 5 5 b . 
            c b d d d d d 5 5 5 5 5 5 5 b . 
            . c d d d d d d 5 5 5 5 5 d b . 
            . . c b d d d d d 5 5 5 b b . . 
            . . . c c c c c c c c b b . . .
    `, SpriteKind.Enemy)
MeBoi.setScale(2, ScaleAnchor.Middle)
Mister_Bad_Guy.setScale(2, ScaleAnchor.Middle)
Mister_Bad_Guy.setPosition(150, 100)
MeBoiHealth = statusbars.create(20, 4, StatusBarKind.Health)
MisterBadGuyHealth = statusbars.create(20, 4, StatusBarKind.EnemyHealth)
MisterBadGuyHealth.attachToSprite(Mister_Bad_Guy)
controller.moveSprite(MeBoi)
MeBoiHealth.setLabel("HP")
MeBoiHealth.attachToSprite(MeBoi)
MeBoi.setStayInScreen(true)
Mister_Bad_Guy.follow(MeBoi, 35)
MeBoiHealth.value += 10
MisterBadGuyHealth.value += 20
