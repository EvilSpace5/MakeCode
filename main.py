def on_on_zero(status2):
    game.game_over(False)
    game.splash("YOU LOSE")
statusbars.on_zero(StatusBarKind.health, on_on_zero)

def on_on_overlap(sprite2, otherSprite2):
    MeBoiHealth.value += -1
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

def on_on_zero2(status):
    game.game_over(True)
    game.splash("YOU WIN")
statusbars.on_zero(StatusBarKind.enemy_health, on_on_zero2)

def on_combos_attach_combo():
    MeBoiHealth.max += 500
    MeBoiHealth.value = 500
controller.combos.attach_combo("uuddlrlrab", on_combos_attach_combo)

def on_combos_attach_combo2():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
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
        """),
        MeBoi,
        50,
        1)
    projectile.set_scale(1.25, ScaleAnchor.MIDDLE)
controller.combos.attach_combo("ua", on_combos_attach_combo2)

def on_on_overlap2(sprite, otherSprite):
    MisterBadGuyHealth.value += -1
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

projectile: Sprite = None
MisterBadGuyHealth: StatusBarSprite = None
MeBoiHealth: StatusBarSprite = None
MeBoi: Sprite = None
scene.set_background_color(14)
music.play(music.string_playable("B A G A G F A C5 ", 120),
    music.PlaybackMode.UNTIL_DONE)
controller.combos.set_extended_combo_mode(True)
MeBoi = sprites.create(img("""
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
    """),
    SpriteKind.player)
Mister_Bad_Guy = sprites.create(img("""
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
    """),
    SpriteKind.enemy)
MeBoi.set_scale(2, ScaleAnchor.MIDDLE)
Mister_Bad_Guy.set_scale(2, ScaleAnchor.MIDDLE)
Mister_Bad_Guy.set_position(150, 100)
MeBoiHealth = statusbars.create(20, 4, StatusBarKind.health)
MisterBadGuyHealth = statusbars.create(20, 4, StatusBarKind.enemy_health)
MisterBadGuyHealth.attach_to_sprite(Mister_Bad_Guy)
controller.move_sprite(MeBoi)
MeBoiHealth.set_label("HP")
MeBoiHealth.attach_to_sprite(MeBoi)
MeBoi.set_stay_in_screen(True)
Mister_Bad_Guy.follow(MeBoi, 35)
MeBoiHealth.value += 10
MisterBadGuyHealth.value += 20