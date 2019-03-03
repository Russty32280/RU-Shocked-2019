/*
 * IEEE1451_001.c
 *
 *  Created on: Feb 18, 2019
 *      Author: Russty
 */


int S_Channel[MAX_NUMBER_OF_CHANNELS] = [0,0,0,0,0,0];
int K_Channel[MAX_NUMBER_OF_CHANNELS] = [0,0,0,0,0,0];
int J_Channel[MAX_NUMBER_OF_CHANNELS] = [0,0,0,0,0,0];
int Up_Channel[MAX_NUMBER_OF_CHANNELS] = [0,0,0,0,0,0];
int Dwn_Channel[MAX_NUMBER_OF_CHANNELS] = [0,0,0,0,0,0];
int Equal_Channel[MAX_NUMBER_OF_CHANNELS] = [0,0,0,0,0,0];
int MaxLengths[MAX_NUMBER_OF_CHANNELS] = [3, 3, 3, 3, 3, 3];
int ChannelErrors[MAX_NUMBER_OF_CHANNELS] = [0, 0, 0, 0, 0, 0];
int ChannelStatus[MAX_NUMBER_OF_CHANNELS] = [0, 0, 0, 0, 0, 0];
double Signal[MAX_NUMBER_OF_CHANNELS][MAX_SIGNAL_LENGTH];


int Segmentation_Init()
{
    S_Channel = [0,0,0,0,0,0];
    K_Channel = [0,0,0,0,0,0];
    J_Channel = [0,0,0,0,0,0];
    Up_Channel = [0,0,0,0,0,0];
    Dwn_Channel = [0,0,0,0,0,0];
    Equal_Channel = [0,0,0,0,0,0];
    return 0;
}

int Segmentation_AddChannel(char SensorChannel, int Error, int MaxSegLength)
{
    if(SensorChannel > MAX_NUMNBER_OF_CHANNELS || SensorChannel < 0)
        return SENSOR_CHANNEL_OUT_OF_RANGE;
    if(ChannelError > MAX_ERROR)
        return CHANNEL_ERROR_OUT_OF_RANGE;
    if(MaxSegLength > MAX_LENGTH)
        return MAX_SEGMENT_LENGTH_OUT_OF_RANGE;

    ChannelErrors[SensorChannel] = Error;
    MaxLengths[SensorChannel] = MaxSegLength;
    ChannelStatus[SensorChannel] = 1;
    return 0;
}

int Segmentation_ModifiyChannelError(char SensorChannel, int NewError)
{
    if(SensorChannel > MAX_NUMNBER_OF_CHANNELS || SensorChannel < 0)
        return SENSOR_CHANNEL_OUT_OF_RANGE;
    if(NewError > MAX_ERROR)
        return CHANNEL_ERROR_OUT_OF_RANGE;
    ChannelErrors[SensorChannel] = NewError;
    return 0;
}

int Segmentation_ModifyChannelSegLength(char SensorChannel, int NewMaxSegLength)
{
    if(SensorChannel > MAX_NUMNBER_OF_CHANNELS || SensorChannel < 0)
        return SENSOR_CHANNEL_OUT_OF_RANGE;
    if(NewMaxSegLength > MAX_LENGTH)
        return MAX_SEGMENT_LENGTH_OUT_OF_RANGE;
    MaxLengths[SensorChannel] = NewMaxSegLength;
    return 0;
}

int Segmentation_DisableChannel(char SensorChannel)
{
    if(SensorChannel > MAX_NUMNBER_OF_CHANNELS || SensorChannel < 0)
        return SENSOR_CHANNEL_OUT_OF_RANGE;
    ChannelStatus[SensorChannel] = 0;
    return 0;
}

int Segmentation_EnableChannel(char SensorChannel)
{
    if(SensorChannel > MAX_NUMNBER_OF_CHANNELS || SensorChannel < 0)
        return SENSOR_CHANNEL_OUT_OF_RANGE;
    ChannelStatus[SensorChannel] = 1;
    return 0;
}



int Segmentation_AddNewData(char SensorChannel, double SensorData)
{
    if(SensorChannel > MAX_NUMNBER_OF_CHANNELS || SensorChannel < 0)
        return SENSOR_CHANNEL_OUT_OF_RANGE;

    ModStep[SensorChannel] = K_Channel[SensorChannel] % 2;

    //Initial Sample
    if(K == 0){
        Signal[SensorChannel][K] = SensorData;
        K_Channel[SensorChannel]++;
        J_Channel[SensorChannel]++;
    }
    else {
        switch(ModStep[SensorChannel]){
        case 0:
            Signal[SensorChannel][K] = SensorData;
            Dif_Channel[SensorChannel] = (Signal[SensorChannel][0] + Signal[SensorChannel][K])/2 - Signal[SensorChannel][J];
            if(Dif_Channel[SensorChannel] > 0)
                Up_Channel[SensorChannel]++;
            else if (Dif_Channel[SensorChannel] < 0)
                Dwn_Channel[SensorChannel]++;
            else
                Equal_Channel[SensorChannel]++;

            if(K_Channels[SensorChannel]==MaxLengths[SensorChannel]){
                if(Signal[SensorChannel][0] = Signal[SensorChannel][K])
                    Class_Channel[SensorChannel] = 'a';
                else if (Signal[SensorChannel][0] < Signal[SensorChannel])
                    Class_Channel[SensorChannel] = 'b';
                else
                    Class_Channel[SensorChannel] = 'c';

                Mark_Channel[SensorChannel] = Signal[SensorChannel][K];
                Time_Channel[SensorChannel] = Time_Channel[SensorChannel]+K;
                Signal[SensorChannel][0] = Signal[SensorChannel][K];
                K_Channel[SensorChannel] = 0;
                J_Channel[SensorChannel] = 0;
                Up_Channel[SensorChannel] = 0;
                Dwn_Channel[SensorChannel] = 0;
                Equal_Channel[SensorChannel] = 0;
                Channel_Status[SensorChannel] = 3;  // 3 is Channel enabled and Segment is Ready to be Read.
            }
            else if (abs(Dif_Channel[SensorChannel]) >= ChannelError[SensorChannel]){
                if(Up_Channel[SensorChannel] > Dwn_Channel[SensorChannel]){
                    if(Signal[SensorChannel][0] > Signal[SensorChannel][K])
                        Class_Channel[SensorChannel] = 'f';
                    else
                        Class_Channel[SensorChannel] = 'd';
                }
                else if (Up_Channel[SensorChannel] < Dwn_Channel[SensorChannel]){
                    if(Signal[SensorChannel][0] > Signal[SensorChannel][K])
                        Class_Channel[SensorChannel] = 'e';
                    else
                        Class_Channel[SensorChannel] = 'g';
                }
                else
                    Class_Channel[SensorChannel] = 'h';


                Mark_Channel[SensorChannel] = Signal[SensorChannel][K];
                Time_Channel[SensorChannel] = Time_Channel[SensorChannel]+K;
                Signal[SensorChannel][0] = Signal[SensorChannel][K];
                K_Channel[SensorChannel] = 0;
                J_Channel[SensorChannel] = 0;
                Up_Channel[SensorChannel] = 0;
                Dwn_Channel[SensorChannel] = 0;
                Equal_Channel[SensorChannel] = 0;
                Channel_Status[SensorChannel] = 3;  // 3 is Channel enabled and Segment is Ready to be Read.
            }

            else{
                J++;
                K++;
            }


            break;
        case 1:
            Signal[SensorChannel][K] = SensorData;
            K++;
            break;


    }

    }

    return 0;
}

int Segmentation_ReadCurrentSegment(char SensorChannel)
{


    return 0;
}


int Segmentation_BeginNewSegment(char SensorChannel)
{
    if(SensorChannel > MAX_NUMNBER_OF_CHANNELS || SensorChannel < 0)
        return SENSOR_CHANNEL_OUT_OF_RANGE;

    S = 0;
    K = 0;
    J = 0;
    Up = 0;
    Dwn = 0;
    Equal = 0;

    return 0;
}

int Segmentation_SetError(char SensorChannel, double Error)
{

    return 0;
}

