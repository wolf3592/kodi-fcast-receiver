import xbmc
import xbmcgui

from .FCastSession import FCastSession, PlayBackUpdateMessage, PlayBackState, PlayMessage,OpCode
from .util import log

from typing import List, Optional

class FCastPlayer(xbmc.Player):
    playback_speed: float = 1.0
    sessions: List[FCastSession]
    is_paused: bool = False
    # Used to perform time updates
    prev_time: int = -1
    
    def __init__(self, sessions: List[FCastSession]):
        self.sessions = sessions
        super().__init__()

    def doPause(self) -> None:
        if not self.is_paused:
            self.is_paused = True
            self.pause()
    
    def doResume(self) -> None:
        if self.is_paused:
            self.is_paused = False
            self.pause()

    def onAVStarted(self) -> None:
        log("Playback started")
        self.is_paused = False
        # Start time loop once the player is active
        #self.onPlayBackTimeChanged()

    def onPlayBackStopped(self) -> None:
        log("Playback stopped")
        self.onPlayBackEnded()

    def onPlayBackPaused(self) -> None:
        self.is_paused = True
        self.onPlayBackTimeChanged()

    def onPlayBackResumed(self) -> None:
        if self.is_paused:
            self.is_paused = False          
    
    def onPlayBackEnded(self) -> None:
        log("Playback ended")
        for session in self.sessions:
            session.sendOpCode(opcode=OpCode.STOP)           
            session.send_playback_update(PlayBackUpdateMessage(
                0,
                PlayBackState.IDLE,
                duration=0
            ))
    
    def onPlayBackError(self) -> None:
        log("Playback error")
        self.onPlayBackEnded()
    
    def onPlayBackSpeedChanged(self, speed: int) -> None:
        self.playback_speed = speed
    
    # Not overriden
    def onPlayBackTimeChanged(self) -> None:
        time_int = int(self.getTime())
        duration=int(self.getTotalTime())
        self.prev_time = int(self.getTime())
        pb_message = PlayBackUpdateMessage(
            time_int,
            PlayBackState.PAUSED if self.is_paused else PlayBackState.PLAYING,
            duration=duration
        )
        for session in self.sessions:
            session.send_playback_update(pb_message)
    
    def addSession(self, session: FCastSession):
        self.sessions.append(session)
    
    def removeSession(self, session: FCastSession):
        self.sessions.remove(session)   

    def isPaused(self) -> bool:
        return self.is_paused

