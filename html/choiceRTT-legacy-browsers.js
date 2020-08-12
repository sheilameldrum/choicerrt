﻿/****************** 
 * Choicertt Test *
 ******************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'choiceRTT';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instructionsRoutineBegin());
flowScheduler.add(instructionsRoutineEachFrame());
flowScheduler.add(instructionsRoutineEnd());
const practiceTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practiceTrialsLoopBegin, practiceTrialsLoopScheduler);
flowScheduler.add(practiceTrialsLoopScheduler);
flowScheduler.add(practiceTrialsLoopEnd);
flowScheduler.add(startTaskRoutineBegin());
flowScheduler.add(startTaskRoutineEachFrame());
flowScheduler.add(startTaskRoutineEnd());
const mainTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(mainTrialsLoopBegin, mainTrialsLoopScheduler);
flowScheduler.add(mainTrialsLoopScheduler);
flowScheduler.add(mainTrialsLoopEnd);
flowScheduler.add(thanksRoutineBegin());
flowScheduler.add(thanksRoutineEachFrame());
flowScheduler.add(thanksRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.2';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var instructionsClock;
var instr;
var startInst;
var startMouse;
var mainClock;
var pos1;
var pos2;
var pos3;
var pos4;
var targImage;
var response;
var mouseResp;
var startTaskClock;
var ready;
var go;
var mouseGo;
var thanksClock;
var text;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  instr = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr',
    text: "In this task you will push the c, v, b, and n keys whenever you see the target 'X' appear in one of the four boxes.\n\nFirst, we shall have a practice.\n\nPush space bar or click/touch to begin the practice session.",
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  startInst = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  startMouse = new core.Mouse({
    win: psychoJS.window,
  });
  startMouse.mouseClock = new util.Clock();
  // Initialize components for Routine "main"
  mainClock = new util.Clock();
  pos1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'pos1', units : 'height', 
    image : 'plainWhite.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  pos2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'pos2', units : 'height', 
    image : 'plainWhite.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  pos3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'pos3', units : 'height', 
    image : 'plainWhite.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  pos4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'pos4', units : 'height', 
    image : 'plainWhite.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  targImage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'targImage', units : 'height', 
    image : 'tarX.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  mouseResp = new core.Mouse({
    win: psychoJS.window,
  });
  mouseResp.mouseClock = new util.Clock();
  // Initialize components for Routine "startTask"
  startTaskClock = new util.Clock();
  ready = new visual.TextStim({
    win: psychoJS.window,
    name: 'ready',
    text: 'Now we shall begin the actual experiment.\n\nReady?\n\nPush space bar or click/touch to begin.',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  go = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  mouseGo = new core.Mouse({
    win: psychoJS.window,
  });
  mouseGo.mouseClock = new util.Clock();
  // Initialize components for Routine "main"
  mainClock = new util.Clock();
  pos1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'pos1', units : 'height', 
    image : 'plainWhite.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  pos2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'pos2', units : 'height', 
    image : 'plainWhite.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  pos3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'pos3', units : 'height', 
    image : 'plainWhite.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  pos4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'pos4', units : 'height', 
    image : 'plainWhite.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  targImage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'targImage', units : 'height', 
    image : 'tarX.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  mouseResp = new core.Mouse({
    win: psychoJS.window,
  });
  mouseResp.mouseClock = new util.Clock();
  // Initialize components for Routine "thanks"
  thanksClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Thanks you for participanting!\n\nThis part of experiment is now over.',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _startInst_allKeys;
var gotValidClick;
var instructionsComponents;
function instructionsRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instructions'-------
    t = 0;
    instructionsClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    startInst.keys = undefined;
    startInst.rt = undefined;
    _startInst_allKeys = [];
    // setup some python lists for storing info about the startMouse
    gotValidClick = false; // until a click is received
    startMouse.mouseClock.reset();
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(instr);
    instructionsComponents.push(startInst);
    instructionsComponents.push(startMouse);
    
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
var prevButtonState;
function instructionsRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instructions'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr* updates
    if (t >= 0.0 && instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr.tStart = t;  // (not accounting for frame time here)
      instr.frameNStart = frameN;  // exact frame index
      
      instr.setAutoDraw(true);
    }

    
    // *startInst* updates
    if (t >= 0.0 && startInst.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startInst.tStart = t;  // (not accounting for frame time here)
      startInst.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { startInst.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { startInst.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { startInst.clearEvents(); });
    }

    if (startInst.status === PsychoJS.Status.STARTED) {
      let theseKeys = startInst.getKeys({keyList: [], waitRelease: false});
      _startInst_allKeys = _startInst_allKeys.concat(theseKeys);
      if (_startInst_allKeys.length > 0) {
        startInst.keys = _startInst_allKeys[_startInst_allKeys.length - 1].name;  // just the last key pressed
        startInst.rt = _startInst_allKeys[_startInst_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // *startMouse* updates
    if (t >= 0.0 && startMouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startMouse.tStart = t;  // (not accounting for frame time here)
      startMouse.frameNStart = frameN;  // exact frame index
      
      startMouse.status = PsychoJS.Status.STARTED;
      prevButtonState = startMouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (startMouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      let buttons = startMouse.getPressed();
      if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = buttons;
        if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionsRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instructions'-------
    instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for thisExp (ExperimentHandler)
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var practiceTrials;
var currentLoop;
function practiceTrialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  practiceTrials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'srttPractice.xlsx',
    seed: undefined, name: 'practiceTrials'
  });
  psychoJS.experiment.addLoop(practiceTrials); // add the loop to the experiment
  currentLoop = practiceTrials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  practiceTrials.forEach(function() {
    const snapshot = practiceTrials.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(mainRoutineBegin(snapshot));
    thisScheduler.add(mainRoutineEachFrame(snapshot));
    thisScheduler.add(mainRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function practiceTrialsLoopEnd() {
  psychoJS.experiment.removeLoop(practiceTrials);

  return Scheduler.Event.NEXT;
}


var mainTrials;
function mainTrialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  mainTrials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.FULLRANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'srttConditions.xlsx',
    seed: undefined, name: 'mainTrials'
  });
  psychoJS.experiment.addLoop(mainTrials); // add the loop to the experiment
  currentLoop = mainTrials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  mainTrials.forEach(function() {
    const snapshot = mainTrials.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(mainRoutineBegin(snapshot));
    thisScheduler.add(mainRoutineEachFrame(snapshot));
    thisScheduler.add(mainRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function mainTrialsLoopEnd() {
  psychoJS.experiment.removeLoop(mainTrials);

  return Scheduler.Event.NEXT;
}


var _response_allKeys;
var mainComponents;
function mainRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'main'-------
    t = 0;
    mainClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    pos1.setPos([(- 0.375), 0]);
    pos2.setPos([(- 0.125), 0]);
    pos3.setPos([0.125, 0]);
    pos4.setPos([0.375, 0]);
    targImage.setPos([xPos, 0]);
    response.keys = undefined;
    response.rt = undefined;
    _response_allKeys = [];
    // setup some python lists for storing info about the mouseResp
    mouseResp.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    mainComponents = [];
    mainComponents.push(pos1);
    mainComponents.push(pos2);
    mainComponents.push(pos3);
    mainComponents.push(pos4);
    mainComponents.push(targImage);
    mainComponents.push(response);
    mainComponents.push(mouseResp);
    
    mainComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function mainRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'main'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = mainClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *pos1* updates
    if (t >= 0 && pos1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pos1.tStart = t;  // (not accounting for frame time here)
      pos1.frameNStart = frameN;  // exact frame index
      
      pos1.setAutoDraw(true);
    }

    
    // *pos2* updates
    if (t >= 0 && pos2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pos2.tStart = t;  // (not accounting for frame time here)
      pos2.frameNStart = frameN;  // exact frame index
      
      pos2.setAutoDraw(true);
    }

    
    // *pos3* updates
    if (t >= 0 && pos3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pos3.tStart = t;  // (not accounting for frame time here)
      pos3.frameNStart = frameN;  // exact frame index
      
      pos3.setAutoDraw(true);
    }

    
    // *pos4* updates
    if (t >= 0 && pos4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pos4.tStart = t;  // (not accounting for frame time here)
      pos4.frameNStart = frameN;  // exact frame index
      
      pos4.setAutoDraw(true);
    }

    
    // *targImage* updates
    if (t >= isi && targImage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      targImage.tStart = t;  // (not accounting for frame time here)
      targImage.frameNStart = frameN;  // exact frame index
      
      targImage.setAutoDraw(true);
    }

    
    // *response* updates
    if (t >= isi && response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response.tStart = t;  // (not accounting for frame time here)
      response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { response.clearEvents(); });
    }

    if (response.status === PsychoJS.Status.STARTED) {
      let theseKeys = response.getKeys({keyList: ['c', 'v', 'b', 'n'], waitRelease: false});
      _response_allKeys = _response_allKeys.concat(theseKeys);
      if (_response_allKeys.length > 0) {
        response.keys = _response_allKeys[_response_allKeys.length - 1].name;  // just the last key pressed
        response.rt = _response_allKeys[_response_allKeys.length - 1].rt;
        // was this correct?
        if (response.keys == corrAns) {
            response.corr = 1;
        } else {
            response.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // *mouseResp* updates
    if (t >= isi && mouseResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouseResp.tStart = t;  // (not accounting for frame time here)
      mouseResp.frameNStart = frameN;  // exact frame index
      
      mouseResp.status = PsychoJS.Status.STARTED;
      mouseResp.mouseClock.reset();
      prevButtonState = mouseResp.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouseResp.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      let buttons = mouseResp.getPressed();
      if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = buttons;
        if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [targImage]) {
            if (obj.contains(mouseResp)) {
              gotValidClick = true;
              mouseResp.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    mainComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function mainRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'main'-------
    mainComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (response.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         response.corr = 1;  // correct non-response
      } else {
         response.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('response.keys', response.keys);
    psychoJS.experiment.addData('response.corr', response.corr);
    if (typeof response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('response.rt', response.rt);
        routineTimer.reset();
        }
    
    response.stop();
    // store data for thisExp (ExperimentHandler)
    const xys = mouseResp.getPos();
    const buttons = mouseResp.getPressed();
    psychoJS.experiment.addData('mouseResp.x', xys[0]);
    psychoJS.experiment.addData('mouseResp.y', xys[1]);
    psychoJS.experiment.addData('mouseResp.leftButton', buttons[0]);
    psychoJS.experiment.addData('mouseResp.midButton', buttons[1]);
    psychoJS.experiment.addData('mouseResp.rightButton', buttons[2]);
    if (mouseResp.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouseResp.clicked_name', mouseResp.clicked_name[0]);}
    // the Routine "main" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _go_allKeys;
var startTaskComponents;
function startTaskRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'startTask'-------
    t = 0;
    startTaskClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    go.keys = undefined;
    go.rt = undefined;
    _go_allKeys = [];
    // setup some python lists for storing info about the mouseGo
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    startTaskComponents = [];
    startTaskComponents.push(ready);
    startTaskComponents.push(go);
    startTaskComponents.push(mouseGo);
    
    startTaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function startTaskRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'startTask'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = startTaskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ready* updates
    if (t >= 0.0 && ready.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ready.tStart = t;  // (not accounting for frame time here)
      ready.frameNStart = frameN;  // exact frame index
      
      ready.setAutoDraw(true);
    }

    
    // *go* updates
    if (t >= 0.0 && go.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      go.tStart = t;  // (not accounting for frame time here)
      go.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { go.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { go.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { go.clearEvents(); });
    }

    if (go.status === PsychoJS.Status.STARTED) {
      let theseKeys = go.getKeys({keyList: [], waitRelease: false});
      _go_allKeys = _go_allKeys.concat(theseKeys);
      if (_go_allKeys.length > 0) {
        go.keys = _go_allKeys[_go_allKeys.length - 1].name;  // just the last key pressed
        go.rt = _go_allKeys[_go_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // *mouseGo* updates
    if (t >= 0.0 && mouseGo.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouseGo.tStart = t;  // (not accounting for frame time here)
      mouseGo.frameNStart = frameN;  // exact frame index
      
      mouseGo.status = PsychoJS.Status.STARTED;
      mouseGo.mouseClock.reset();
      prevButtonState = mouseGo.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouseGo.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      let buttons = mouseGo.getPressed();
      if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = buttons;
        if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    startTaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function startTaskRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'startTask'-------
    startTaskComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for thisExp (ExperimentHandler)
    // the Routine "startTask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var thanksComponents;
function thanksRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'thanks'-------
    t = 0;
    thanksClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    thanksComponents = [];
    thanksComponents.push(text);
    
    thanksComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function thanksRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'thanks'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = thanksClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    thanksComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function thanksRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'thanks'-------
    thanksComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
