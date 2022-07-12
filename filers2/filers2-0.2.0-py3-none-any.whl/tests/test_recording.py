import time


def test_player():
    from filers2.recording import FilersPlayer
    from cpl_media.ffmpeg import FFmpegPlayer
    player = FilersPlayer()
    ff_player = player.ffmpeg_player
    assert isinstance(ff_player, FFmpegPlayer)

    player.clean_up()
