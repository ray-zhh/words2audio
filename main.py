#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: ray
# email: bigboyhonghong@163.com
# time: 2022/12/1 13:18
import pyttsx3


class Words2Audio:
    def __init__(self):
        self.words_file = './words.txt'
        self.speaker = pyttsx3.init()
        self.words = self.get_words()

    def get_words(self):
        """
        读取文件内容
        :return:
        """
        with open(self.words_file, 'r', encoding='utf-8') as f:
            return f.read()

    def say_words(self):
        """
        讲述内容
        :return:
        """
        self.speaker.say(self.words)
        self.speaker.runAndWait()

    def save_audio_file(self):
        """
        保存到音频文件
        :return:
        """
        self.speaker.save_to_file(self.words, r'./words.mp3')
        self.speaker.runAndWait()


if __name__ == '__main__':
    Words2Audio().say_words()
