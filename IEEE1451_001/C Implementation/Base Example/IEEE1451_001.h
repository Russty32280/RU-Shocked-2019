/*
 * IEEE1451_001.h
 *
 *  Created on: Feb 18, 2019
 *      Author: Russty
 */

#ifndef IEEE1451_001_H_
#define IEEE1451_001_H_

#define MAX_NUMBER_OF_CHANNELS 6
#define MAX_ERROR 65535
#define MAX_LENGTH 65535


#define SENSOR_CHANNEL_OUT_OF_RANGE     1
#define CHANNEL_ERROR_OUT_OF_RANGE      2
#define MAX_SEGMENT_LENGTH_OUT_OF_RANGE 3


int Segmentation_Init()
int Segmentation_AddChannel(char SensorChannel, int Error)
int Segmentation_WriteNewData(char SensorChannel, double SensorData)
int Segmentation_ReadCurrentSegments(char SensorChannel)
int Segmentation_BeginNewSegment(char SensorChannel)
int Segmentation_SetError(char SensorChannel)


#endif /* IEEE1451_001_H_ */
