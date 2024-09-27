#!/usr/bin/python3

# -*- coding:utf-8 -*-

import os
import cv2 as cv

class Cam:
    def __init__(self, login:str, passwd:str, ip:str, root_folder:str, port:str='554', thread:str='main') -> None:
        self.__login = login
        self.__passwd = passwd
        self.__ip = ip
        self.__port = port
        self.__thread = thread
        self.__rtsp_url = f'rtsp://{self.__login}:{self.__passwd}@{self.__ip}:{self.__port}/{self.__thread}'
        self.__save_folder = os.path.join(root_folder, f'cam_{self.__ip.split('.')[-1]}')
        self.__len_num = 12
        self.__screen_format = '.png'
        self.__current_num = self.__get_first_num()
    
    def __get_first_num(self) -> int:
        if not os.path.isdir(self.__save_folder):
            os.system(f'mkdir {self.__save_folder}')
            return 0
        files_num = [
            int(f.replace(self.__screen_format), '') for f in os.listdir(self.__save_folder) if f.endswith(self.__screen_format)
        ]
        if len(files_num) == 0:
            return 0
        last_files_num = max(files_num)
        return last_files_num + 1
    
    def __next_file_name(self) -> str:
        num = str(self.__current_num)
        if len(num) < self.__len_num:
            zero_count = self.__len_num - len(num)
            num = '0'*zero_count + num
        file_name = num + self.__screen_format
        file_path = os.path.join(self.__save_folder, file_name)
        self.__current_num += 1
        return file_path
    
    def save(self) -> None:
        save_path = self.__next_file_name()
        cap = cv.VideoCapture(self.__rtsp_url, cv.CAP_FFMPEG)
        if not cap.isOpened():
            print(f'Can not open stream for cam_ip: {self.__ip}')
            return
        _, frame = cap.read()
        cv.imwrite(save_path, frame)
        cap.release()
