class bucketsgame:
    def __init__(self):
        self.b3_capacity = 3
        self.b5_capacity = 5
        self.b8_capacity = 8

        self.b3 = 0  
        self.b5 = 0  
        self.b8 = 8  

    def display_state(self):
        print(f"{'8|':<2} {' ' * (self.b8_capacity - self.b8)}{'W' * self.b8}|")
        for i in range(7, 0, -1):
            print(f"{i}|")
        print(f"+{'-' * 6}+ +{'-' * 6}+ +{'-' * 6}+")
        print(f"{'8L':<8}{'5L':<8}{'3L'}")
        print()

    def fill(self, bucket):
        if bucket == 3:
            self.b3 = self.b3_capacity
        elif bucket == 5:
            self.b5 = self.b5_capacity
        elif bucket == 8:
            self.b8 = self.b8_capacity
        self.display_state()

    def empty(self, bucket):
        if bucket == 3:
            self.b3 = 0
        elif bucket == 5:
            self.b5 = 0
        elif bucket == 8:
            self.b8 = 0
        self.display_state()

    def pour(self, from_bucket, to_bucket):
        if from_bucket == 8:
            from_capacity = self.b8
        elif from_bucket == 5:
            from_capacity = self.b5
        elif from_bucket == 3:
            from_capacity = self.b3

        if to_bucket == 8:
            to_capacity = self.b8_capacity
            to_current = self.b8
        elif to_bucket == 5:
            to_capacity = self.b5_capacity
            to_current = self.b5
        elif to_bucket == 3:
            to_capacity = self.b3_capacity
            to_current = self.b3

        transfer = min(from_capacity, to_capacity - to_current)

        if from_bucket == 8:
            self.b8 -= transfer
        elif from_bucket == 5:
            self.b5 -= transfer
        elif from_bucket == 3:
            self.b3 -= transfer

        if to_bucket == 8:
            self.b8 += transfer
        elif to_bucket == 5:
            self.b5 += transfer
        elif to_bucket == 3:
            self.b3 += transfer

        self.display_state()

    def game_loop(self):
        print("Water Bucket Puzzle")
        print("Try to get 4L of water into one of these buckets:\n")

        while True:
            self.display_state()
            print("You can:")
            print(" (F)ill the bucket")
            print(" (E)mpty the bucket")
            print(" (P)our one bucket into another")
            print(" (Q)uit")
            choice = input("> ").lower()

            if choice == 'q':
                print("Goodbye!")
                break
            elif choice == 'f':
                bucket = int(input("Select a bucket 8, 5, 3: "))
                self.fill(bucket)
            elif choice == 'e':
                bucket = int(input("Select a bucket 8, 5, 3: "))
                self.empty(bucket)
            elif choice == 'p':
                from_bucket = int(input("Pour from bucket 8, 5, 3: "))
                to_bucket = int(input("Pour into bucket 8, 5, 3: "))
                self.pour(from_bucket, to_bucket)

            if self.b5 == 4 or self.b3 == 4 or self.b8 == 4:
                print("Congratulations! You have exactly 4 liters!")
                break

game = bucketsgame()
game.game_loop()
