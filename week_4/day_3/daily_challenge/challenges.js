// Exercise : Video Class
class Video {
  constructor(title, uploader, time) {
    this.title = title;
    this.uploader = uploader;
    this.time = time;
  }

  watch() {
    console.log(
      `${this.uploader} watched all ${this.time} seconds of ${this.title}!`
    );
  }
}

// Create 2 video instances
const video1 = new Video("Learn JavaScript OOP", "Alice", 300);
video1.watch();

const video2 = new Video("Intro to Node.js", "Bob", 450);
video2.watch();

// Bonus: store 5 videos in an array
const videoData = [
  ["React Tutorial", "Charlie", 600],
  ["CSS Animations", "Diana", 200],
  ["Python Basics", "Eve", 800],
  ["SQL Crash Course", "Frank", 700],
  ["Rust Programming", "Grace", 500],
];

// Instantiate and call watch for each
const videos = videoData.map(
  ([title, uploader, time]) => new Video(title, uploader, time)
);

videos.forEach((video) => video.watch());
