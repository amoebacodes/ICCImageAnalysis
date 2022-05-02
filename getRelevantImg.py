"""
input:
    task: a task from taskDict keys
    dicts: made prior to general process in the notebook
    keys: the keys of the normalized image dictionary (get image names)
output:
    indices of relevant images to the task in keys
    [[condition 0[channel 0[], channel 1[]]], [condition 1[channel0[], channel1[]]]]
"""
def getRelevantImg(task:str, taskDict, conditionRegexDict, chRegexDict, keys:list):
    conditions = taskDict[task][0]
    channels = taskDict[task][1]
    keysIdx = []
    for condition in conditions:
        cond = []
        for channel in channels:
            ch = []
            for i in range(len(keys)):
                if conditionRegexDict[condition].search(keys[i]) != None and chRegexDict[channel].search(keys[i]) != None:
                    ch.append(i)
            if ch:
                cond.append(ch)
        if cond:
            keysIdx.append(cond)
    return keysIdx