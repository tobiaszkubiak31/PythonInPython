from multiprocessing import Process
import launcher
import launcher_copy_for_testing


if __name__ == '__main__':
    client1 = Process(target=launcher.main)
    client2 = Process(target=launcher_copy_for_testing.main)
    client1.start()
    client2.start()
