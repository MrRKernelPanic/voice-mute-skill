from mycroft import MycroftSkill, intent_file_handler


class VoiceMute(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('mute.voice.intent')
    def handle_mute_voice(self, message):
        self.speak_dialog('mute.voice')


def create_skill():
    return VoiceMute()

