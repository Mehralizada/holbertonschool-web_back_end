export default function taskBlock(trueOrFalse) {
  let task = false;
  let task2 = true;

  if (trueOrFalse) {
    // Use separate variables for the block scope
    let blockTask = true;
    let blockTask2 = false;

    // Optionally, you can assign these to the outer variables
    // if you want to use them outside the block
    task = blockTask;
    task2 = blockTask2;
  }

  return [task, task2];
}
