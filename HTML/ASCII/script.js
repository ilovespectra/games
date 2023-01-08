function convertImage() {
  // Get the input image and reset the progress bar
  const inputImage = document.getElementById('input-image');
  if (inputImage === null) {
    console.error('Error: input-image element not found');
    return;
  }
  const file = inputImage.files[0];
  const progressBar = document.getElementById('conversion-progress');
  progressBar.value = 0;

  // Create a file reader to read the image
  const reader = new FileReader();

  // Set the onprogress event handler to update the progress bar
  reader.onprogress = function(event) {
    if (event.lengthComputable) {
      progressBar.value = (event.loaded / event.total) * 100;
    }
  };

  reader.onload = function(event) {
    const image = new Image();
    image.onload = function() {
      // Get the canvas element and set its width and height
      const canvas = document.createElement('canvas');
      canvas.width = image.width;
      canvas.height = image.height;

      // Draw the image on the canvas
      const context = canvas.getContext('2d');
      context.drawImage(image, 0, 0);

      // Get the image data from the canvas
      const imageData = context.getImageData(0, 0, image.width, image.height);

      // Convert the image data to ASCII art
      const output = imageDataToASCII(imageData);

      // Update the src attribute of the output image with the ASCII art
      const outputImage = document.getElementById('output-image');
      outputImage.src = 'data:image/png;base64,' + btoa(output);

      // Update the download link with the ASCII art
      const downloadLink = document.getElementById('download-link');
      downloadLink.href = 'data:text/plain;charset=utf-8,' + encodeURIComponent(output);
      downloadLink.download = 'ascii-art.txt';

      // Display the ASCII art in the output element
      const outputElement = document.getElementById('output');
      outputElement.textContent = output;

      // Reset the progress bar
      progressBar.value = 0;
    };
    image.src = event.target.result;
  };
  reader.readAsDataURL(file);
}

function imageDataToASCII(imageData) {
  // Create an array of ASCII characters to use for the conversion
  const chars = ['@', '#', '$', '=', '*', ':', '-', '.'];

  // Initialize the output string
  let output = '';

  // Iterate over the image data and convert each pixel to ASCII
  for (let i = 0; i < imageData.data.length; i += 4) {
    // Get the red, green, and blue values for the current pixel
    const r = imageData.data[i];
    const g = imageData.data[i + 1];
    const b = imageData.data[i + 2];

    // Calculate the average value of the red, green, and blue values
    const value = (r + g + b) / 3;

    // Map the average value to an ASCII character
    const charIndex = Math.floor(value / 256 * chars.length);
    const char = chars[charIndex];

    // Add the ASCII character to the output string
    output += char;

    // Add a newline after every image width characters
    if ((i / 4 + 1) % imageData.width === 0) {
      output += '\n';
    }
  }

  return output;
}
