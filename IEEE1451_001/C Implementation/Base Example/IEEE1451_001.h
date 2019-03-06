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
int Segmentation_AddChannel(char SensorChannel, int Error, int MaxSegLength)
int Segmentation_ModifiyChannelError(char SensorChannel, int NewError)
int Segmentation_ModifyChannelSegLength(char SensorChannel, int NewMaxSegLength)
int Segmentation_DisableChannel(char SensorChannel)
int Segmentation_EnableChannel(char SensorChannel)
int Segmentation_WriteNewData(char SensorChannel, double SensorData)
int Segmentation_ReadSegmentClass(char SensorChannel)
int Segmentation_ReadSegmentTime(char SensorChannel)
double Segmentation_ReadSegmentMark(char SensorChannel)
int Segmentation_BeginNewSegment(char SensorChannel)


/*
* Status Bits for the Channels
* b0 - Channel enabled
* b1 - Segment is Ready to be read
* b2 - Segment Class is Ready to be Read
* b3 - Segment Time is ready to be Read
* b4 - Segment Mark is Ready to be Read
*/


#endif /* IEEE1451_001_H_ */
