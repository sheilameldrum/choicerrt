#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Tue Aug 11 17:50:25 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'choiceRTT'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/sheilameldrum/Documents/GitHub/choicertt/choiceRTT_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instr = visual.TextStim(win=win, name='instr',
    text="In this task you will push the space bar or click/touch the target whenever you see the target 'X' appear.\n\nFirst, we shall have a practice.\n\nPush space bar or click/touch to begin the practice session.",
    font='Arial',
    units='height', pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
startInst = keyboard.Keyboard()
startMouse = event.Mouse(win=win)
x, y = [None, None]
startMouse.mouseClock = core.Clock()

# Initialize components for Routine "main"
mainClock = core.Clock()
pos1 = visual.ImageStim(
    win=win,
    name='pos1', units='height', 
    image='plainWhite.png', mask=None,
    ori=0, pos=[0,0], size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
pos2 = visual.ImageStim(
    win=win,
    name='pos2', units='height', 
    image='plainWhite.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
pos3 = visual.ImageStim(
    win=win,
    name='pos3', units='height', 
    image='plainWhite.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
pos4 = visual.ImageStim(
    win=win,
    name='pos4', units='height', 
    image='plainWhite.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
targImage = visual.ImageStim(
    win=win,
    name='targImage', units='height', 
    image='tarX.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
response = keyboard.Keyboard()
mouseResp = event.Mouse(win=win)
x, y = [None, None]
mouseResp.mouseClock = core.Clock()

# Initialize components for Routine "startTask"
startTaskClock = core.Clock()
ready = visual.TextStim(win=win, name='ready',
    text='Now we shall begin the actual experiment.\n\nReady?\n\nPush space bar or click/touch to begin.',
    font='Arial',
    units='height', pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
go = keyboard.Keyboard()
mouseGo = event.Mouse(win=win)
x, y = [None, None]
mouseGo.mouseClock = core.Clock()

# Initialize components for Routine "main"
mainClock = core.Clock()
pos1 = visual.ImageStim(
    win=win,
    name='pos1', units='height', 
    image='plainWhite.png', mask=None,
    ori=0, pos=[0,0], size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
pos2 = visual.ImageStim(
    win=win,
    name='pos2', units='height', 
    image='plainWhite.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
pos3 = visual.ImageStim(
    win=win,
    name='pos3', units='height', 
    image='plainWhite.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
pos4 = visual.ImageStim(
    win=win,
    name='pos4', units='height', 
    image='plainWhite.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
targImage = visual.ImageStim(
    win=win,
    name='targImage', units='height', 
    image='tarX.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
response = keyboard.Keyboard()
mouseResp = event.Mouse(win=win)
x, y = [None, None]
mouseResp.mouseClock = core.Clock()

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Thanks you for participanting!\n\nThe experiment is now over.',
    font='Arial',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
startInst.keys = []
startInst.rt = []
_startInst_allKeys = []
# setup some python lists for storing info about the startMouse
gotValidClick = False  # until a click is received
startMouse.mouseClock.reset()
# keep track of which components have finished
instructionsComponents = [instr, startInst, startMouse]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr* updates
    if instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr.frameNStart = frameN  # exact frame index
        instr.tStart = t  # local t and not account for scr refresh
        instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr, 'tStartRefresh')  # time at next scr refresh
        instr.setAutoDraw(True)
    
    # *startInst* updates
    waitOnFlip = False
    if startInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startInst.frameNStart = frameN  # exact frame index
        startInst.tStart = t  # local t and not account for scr refresh
        startInst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startInst, 'tStartRefresh')  # time at next scr refresh
        startInst.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(startInst.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(startInst.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if startInst.status == STARTED and not waitOnFlip:
        theseKeys = startInst.getKeys(keyList=None, waitRelease=False)
        _startInst_allKeys.extend(theseKeys)
        if len(_startInst_allKeys):
            startInst.keys = _startInst_allKeys[-1].name  # just the last key pressed
            startInst.rt = _startInst_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # *startMouse* updates
    if startMouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startMouse.frameNStart = frameN  # exact frame index
        startMouse.tStart = t  # local t and not account for scr refresh
        startMouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startMouse, 'tStartRefresh')  # time at next scr refresh
        startMouse.status = STARTED
        prevButtonState = startMouse.getPressed()  # if button is down already this ISN'T a new click
    if startMouse.status == STARTED:  # only update if started and not finished!
        buttons = startMouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr.started', instr.tStartRefresh)
thisExp.addData('instr.stopped', instr.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('startMouse.started', startMouse.tStart)
thisExp.addData('startMouse.stopped', startMouse.tStop)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practiceTrials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('srttPractice.xlsx'),
    seed=None, name='practiceTrials')
thisExp.addLoop(practiceTrials)  # add the loop to the experiment
thisPracticeTrial = practiceTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
if thisPracticeTrial != None:
    for paramName in thisPracticeTrial:
        exec('{} = thisPracticeTrial[paramName]'.format(paramName))

for thisPracticeTrial in practiceTrials:
    currentLoop = practiceTrials
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
    if thisPracticeTrial != None:
        for paramName in thisPracticeTrial:
            exec('{} = thisPracticeTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "main"-------
    continueRoutine = True
    # update component parameters for each repeat
    pos1.setPos([-.375, 0])
    pos2.setPos([-.125, 0])
    pos3.setPos([.125, 0])
    pos4.setPos([.375, 0])
    targImage.setPos([xPos, 0])
    response.keys = []
    response.rt = []
    _response_allKeys = []
    # setup some python lists for storing info about the mouseResp
    mouseResp.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    mainComponents = [pos1, pos2, pos3, pos4, targImage, response, mouseResp]
    for thisComponent in mainComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    mainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "main"-------
    while continueRoutine:
        # get current time
        t = mainClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=mainClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pos1* updates
        if pos1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pos1.frameNStart = frameN  # exact frame index
            pos1.tStart = t  # local t and not account for scr refresh
            pos1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pos1, 'tStartRefresh')  # time at next scr refresh
            pos1.setAutoDraw(True)
        
        # *pos2* updates
        if pos2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pos2.frameNStart = frameN  # exact frame index
            pos2.tStart = t  # local t and not account for scr refresh
            pos2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pos2, 'tStartRefresh')  # time at next scr refresh
            pos2.setAutoDraw(True)
        
        # *pos3* updates
        if pos3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pos3.frameNStart = frameN  # exact frame index
            pos3.tStart = t  # local t and not account for scr refresh
            pos3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pos3, 'tStartRefresh')  # time at next scr refresh
            pos3.setAutoDraw(True)
        
        # *pos4* updates
        if pos4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pos4.frameNStart = frameN  # exact frame index
            pos4.tStart = t  # local t and not account for scr refresh
            pos4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pos4, 'tStartRefresh')  # time at next scr refresh
            pos4.setAutoDraw(True)
        
        # *targImage* updates
        if targImage.status == NOT_STARTED and tThisFlip >= isi-frameTolerance:
            # keep track of start time/frame for later
            targImage.frameNStart = frameN  # exact frame index
            targImage.tStart = t  # local t and not account for scr refresh
            targImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(targImage, 'tStartRefresh')  # time at next scr refresh
            targImage.setAutoDraw(True)
        
        # *response* updates
        waitOnFlip = False
        if response.status == NOT_STARTED and tThisFlip >= isi-frameTolerance:
            # keep track of start time/frame for later
            response.frameNStart = frameN  # exact frame index
            response.tStart = t  # local t and not account for scr refresh
            response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
            response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response.status == STARTED and not waitOnFlip:
            theseKeys = response.getKeys(keyList=['c', 'v', 'b', 'n'], waitRelease=False)
            _response_allKeys.extend(theseKeys)
            if len(_response_allKeys):
                response.keys = _response_allKeys[-1].name  # just the last key pressed
                response.rt = _response_allKeys[-1].rt
                # was this correct?
                if (response.keys == str(corrAns)) or (response.keys == corrAns):
                    response.corr = 1
                else:
                    response.corr = 0
                # a response ends the routine
                continueRoutine = False
        # *mouseResp* updates
        if mouseResp.status == NOT_STARTED and t >= isi-frameTolerance:
            # keep track of start time/frame for later
            mouseResp.frameNStart = frameN  # exact frame index
            mouseResp.tStart = t  # local t and not account for scr refresh
            mouseResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouseResp, 'tStartRefresh')  # time at next scr refresh
            mouseResp.status = STARTED
            mouseResp.mouseClock.reset()
            prevButtonState = mouseResp.getPressed()  # if button is down already this ISN'T a new click
        if mouseResp.status == STARTED:  # only update if started and not finished!
            buttons = mouseResp.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [targImage]:
                        if obj.contains(mouseResp):
                            gotValidClick = True
                            mouseResp.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mainComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "main"-------
    for thisComponent in mainComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceTrials.addData('pos1.started', pos1.tStartRefresh)
    practiceTrials.addData('pos1.stopped', pos1.tStopRefresh)
    practiceTrials.addData('pos2.started', pos2.tStartRefresh)
    practiceTrials.addData('pos2.stopped', pos2.tStopRefresh)
    practiceTrials.addData('pos3.started', pos3.tStartRefresh)
    practiceTrials.addData('pos3.stopped', pos3.tStopRefresh)
    practiceTrials.addData('pos4.started', pos4.tStartRefresh)
    practiceTrials.addData('pos4.stopped', pos4.tStopRefresh)
    practiceTrials.addData('targImage.started', targImage.tStartRefresh)
    practiceTrials.addData('targImage.stopped', targImage.tStopRefresh)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response.corr = 1;  # correct non-response
        else:
           response.corr = 0;  # failed to respond (incorrectly)
    # store data for practiceTrials (TrialHandler)
    practiceTrials.addData('response.keys',response.keys)
    practiceTrials.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        practiceTrials.addData('response.rt', response.rt)
    practiceTrials.addData('response.started', response.tStartRefresh)
    practiceTrials.addData('response.stopped', response.tStopRefresh)
    # store data for practiceTrials (TrialHandler)
    x, y = mouseResp.getPos()
    buttons = mouseResp.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [targImage]:
            if obj.contains(mouseResp):
                gotValidClick = True
                mouseResp.clicked_name.append(obj.name)
    practiceTrials.addData('mouseResp.x', x)
    practiceTrials.addData('mouseResp.y', y)
    practiceTrials.addData('mouseResp.leftButton', buttons[0])
    practiceTrials.addData('mouseResp.midButton', buttons[1])
    practiceTrials.addData('mouseResp.rightButton', buttons[2])
    if len(mouseResp.clicked_name):
        practiceTrials.addData('mouseResp.clicked_name', mouseResp.clicked_name[0])
    practiceTrials.addData('mouseResp.started', mouseResp.tStart)
    practiceTrials.addData('mouseResp.stopped', mouseResp.tStop)
    # the Routine "main" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'practiceTrials'


# ------Prepare to start Routine "startTask"-------
continueRoutine = True
# update component parameters for each repeat
go.keys = []
go.rt = []
_go_allKeys = []
# setup some python lists for storing info about the mouseGo
gotValidClick = False  # until a click is received
# keep track of which components have finished
startTaskComponents = [ready, go, mouseGo]
for thisComponent in startTaskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "startTask"-------
while continueRoutine:
    # get current time
    t = startTaskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startTaskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ready* updates
    if ready.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ready.frameNStart = frameN  # exact frame index
        ready.tStart = t  # local t and not account for scr refresh
        ready.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ready, 'tStartRefresh')  # time at next scr refresh
        ready.setAutoDraw(True)
    
    # *go* updates
    waitOnFlip = False
    if go.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        go.frameNStart = frameN  # exact frame index
        go.tStart = t  # local t and not account for scr refresh
        go.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(go, 'tStartRefresh')  # time at next scr refresh
        go.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(go.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(go.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if go.status == STARTED and not waitOnFlip:
        theseKeys = go.getKeys(keyList=None, waitRelease=False)
        _go_allKeys.extend(theseKeys)
        if len(_go_allKeys):
            go.keys = _go_allKeys[-1].name  # just the last key pressed
            go.rt = _go_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # *mouseGo* updates
    if mouseGo.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouseGo.frameNStart = frameN  # exact frame index
        mouseGo.tStart = t  # local t and not account for scr refresh
        mouseGo.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouseGo, 'tStartRefresh')  # time at next scr refresh
        mouseGo.status = STARTED
        mouseGo.mouseClock.reset()
        prevButtonState = mouseGo.getPressed()  # if button is down already this ISN'T a new click
    if mouseGo.status == STARTED:  # only update if started and not finished!
        buttons = mouseGo.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startTaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "startTask"-------
for thisComponent in startTaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ready.started', ready.tStartRefresh)
thisExp.addData('ready.stopped', ready.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouseGo.started', mouseGo.tStart)
thisExp.addData('mouseGo.stopped', mouseGo.tStop)
thisExp.nextEntry()
# the Routine "startTask" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
mainTrials = data.TrialHandler(nReps=1, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('srttConditions.xlsx'),
    seed=None, name='mainTrials')
thisExp.addLoop(mainTrials)  # add the loop to the experiment
thisMainTrial = mainTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMainTrial.rgb)
if thisMainTrial != None:
    for paramName in thisMainTrial:
        exec('{} = thisMainTrial[paramName]'.format(paramName))

for thisMainTrial in mainTrials:
    currentLoop = mainTrials
    # abbreviate parameter names if possible (e.g. rgb = thisMainTrial.rgb)
    if thisMainTrial != None:
        for paramName in thisMainTrial:
            exec('{} = thisMainTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "main"-------
    continueRoutine = True
    # update component parameters for each repeat
    pos1.setPos([-.375, 0])
    pos2.setPos([-.125, 0])
    pos3.setPos([.125, 0])
    pos4.setPos([.375, 0])
    targImage.setPos([xPos, 0])
    response.keys = []
    response.rt = []
    _response_allKeys = []
    # setup some python lists for storing info about the mouseResp
    mouseResp.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    mainComponents = [pos1, pos2, pos3, pos4, targImage, response, mouseResp]
    for thisComponent in mainComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    mainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "main"-------
    while continueRoutine:
        # get current time
        t = mainClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=mainClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pos1* updates
        if pos1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pos1.frameNStart = frameN  # exact frame index
            pos1.tStart = t  # local t and not account for scr refresh
            pos1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pos1, 'tStartRefresh')  # time at next scr refresh
            pos1.setAutoDraw(True)
        
        # *pos2* updates
        if pos2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pos2.frameNStart = frameN  # exact frame index
            pos2.tStart = t  # local t and not account for scr refresh
            pos2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pos2, 'tStartRefresh')  # time at next scr refresh
            pos2.setAutoDraw(True)
        
        # *pos3* updates
        if pos3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pos3.frameNStart = frameN  # exact frame index
            pos3.tStart = t  # local t and not account for scr refresh
            pos3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pos3, 'tStartRefresh')  # time at next scr refresh
            pos3.setAutoDraw(True)
        
        # *pos4* updates
        if pos4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            pos4.frameNStart = frameN  # exact frame index
            pos4.tStart = t  # local t and not account for scr refresh
            pos4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pos4, 'tStartRefresh')  # time at next scr refresh
            pos4.setAutoDraw(True)
        
        # *targImage* updates
        if targImage.status == NOT_STARTED and tThisFlip >= isi-frameTolerance:
            # keep track of start time/frame for later
            targImage.frameNStart = frameN  # exact frame index
            targImage.tStart = t  # local t and not account for scr refresh
            targImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(targImage, 'tStartRefresh')  # time at next scr refresh
            targImage.setAutoDraw(True)
        
        # *response* updates
        waitOnFlip = False
        if response.status == NOT_STARTED and tThisFlip >= isi-frameTolerance:
            # keep track of start time/frame for later
            response.frameNStart = frameN  # exact frame index
            response.tStart = t  # local t and not account for scr refresh
            response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
            response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response.status == STARTED and not waitOnFlip:
            theseKeys = response.getKeys(keyList=['c', 'v', 'b', 'n'], waitRelease=False)
            _response_allKeys.extend(theseKeys)
            if len(_response_allKeys):
                response.keys = _response_allKeys[-1].name  # just the last key pressed
                response.rt = _response_allKeys[-1].rt
                # was this correct?
                if (response.keys == str(corrAns)) or (response.keys == corrAns):
                    response.corr = 1
                else:
                    response.corr = 0
                # a response ends the routine
                continueRoutine = False
        # *mouseResp* updates
        if mouseResp.status == NOT_STARTED and t >= isi-frameTolerance:
            # keep track of start time/frame for later
            mouseResp.frameNStart = frameN  # exact frame index
            mouseResp.tStart = t  # local t and not account for scr refresh
            mouseResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouseResp, 'tStartRefresh')  # time at next scr refresh
            mouseResp.status = STARTED
            mouseResp.mouseClock.reset()
            prevButtonState = mouseResp.getPressed()  # if button is down already this ISN'T a new click
        if mouseResp.status == STARTED:  # only update if started and not finished!
            buttons = mouseResp.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [targImage]:
                        if obj.contains(mouseResp):
                            gotValidClick = True
                            mouseResp.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mainComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "main"-------
    for thisComponent in mainComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    mainTrials.addData('pos1.started', pos1.tStartRefresh)
    mainTrials.addData('pos1.stopped', pos1.tStopRefresh)
    mainTrials.addData('pos2.started', pos2.tStartRefresh)
    mainTrials.addData('pos2.stopped', pos2.tStopRefresh)
    mainTrials.addData('pos3.started', pos3.tStartRefresh)
    mainTrials.addData('pos3.stopped', pos3.tStopRefresh)
    mainTrials.addData('pos4.started', pos4.tStartRefresh)
    mainTrials.addData('pos4.stopped', pos4.tStopRefresh)
    mainTrials.addData('targImage.started', targImage.tStartRefresh)
    mainTrials.addData('targImage.stopped', targImage.tStopRefresh)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response.corr = 1;  # correct non-response
        else:
           response.corr = 0;  # failed to respond (incorrectly)
    # store data for mainTrials (TrialHandler)
    mainTrials.addData('response.keys',response.keys)
    mainTrials.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        mainTrials.addData('response.rt', response.rt)
    mainTrials.addData('response.started', response.tStartRefresh)
    mainTrials.addData('response.stopped', response.tStopRefresh)
    # store data for mainTrials (TrialHandler)
    x, y = mouseResp.getPos()
    buttons = mouseResp.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [targImage]:
            if obj.contains(mouseResp):
                gotValidClick = True
                mouseResp.clicked_name.append(obj.name)
    mainTrials.addData('mouseResp.x', x)
    mainTrials.addData('mouseResp.y', y)
    mainTrials.addData('mouseResp.leftButton', buttons[0])
    mainTrials.addData('mouseResp.midButton', buttons[1])
    mainTrials.addData('mouseResp.rightButton', buttons[2])
    if len(mouseResp.clicked_name):
        mainTrials.addData('mouseResp.clicked_name', mouseResp.clicked_name[0])
    mainTrials.addData('mouseResp.started', mouseResp.tStart)
    mainTrials.addData('mouseResp.stopped', mouseResp.tStop)
    # the Routine "main" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'mainTrials'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [text]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
