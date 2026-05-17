def selectlanguage(self, event):
    self.language = event.GetString()
    self.update_translation()

def update_translation(self):
    """Update the translation based on the selected language"""
    if self.language == 'English':
        self.text = 'Hello, World!'
    elif self.language == 'Spanish':
        self.text = '¡Hola, Mundo!'
    elif self.language == 'French':
        self.text = 'Bonjour, le Monde!'
    elif self.language == 'German':
        self.text = 'Hallo, Welt!'
    elif self.language == 'Italian':
        self.text = 'Ciao, Mondo!'
    elif self.language == 'Portuguese':
        self.text = 'Olá, Mundo!'
    elif self.language == 'Russian':
        self.text = 'Привет, Мир!'
    elif self.language == 'Chinese':
        self.text = '你好，世界！'
    elif self.language == 'Japanese':
        self.text = 'こんにちは、世界！'
    elif self.language == 'Korean':
        self.text = '안녕하세요, 세계!'
    elif self.language == 'Arabic':
        self.text = 'مرحبا بالعالم!'
    elif self.language == 'Hindi':
        self.text = 'नमस्ते, दुनिया!'
    elif self.language == 'Turkish':
        self.text = 'Merhaba, Dünya!'
    elif self.language == 'Dutch':
        self.text = 'Hallo, Wereld!'
    elif self.language == 'Swedish':
        self.text = 'Hej, Världen!'
    elif self.language == 'Norwegian':
        self.text = 'Hei, Verden!'
    elif self.language == 'Danish':
        self.text = 'Hej, Verden!'
    elif self.language == 'Finnish':
        self.text = 'Hei, Maailma!'
    elif self.language == 'Polish':
        self.text = 'Cześć, Świat!'
    elif self.language == 'Ukrainian':
        self.text = 'Привіт, Світ!'