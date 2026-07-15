---
title: "RNHostView"
description: "A component that enables React Native views inside Jetpack Compose."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/rnhostview.md"
scraped_at: "2026-07-15T09:00:46.283974"
---

---
title: RNHostView
description: A component that enables React Native views inside Jetpack Compose.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# RNHostView

A component that enables React Native views inside Jetpack Compose.
Android, Included in Expo Go

A component that enables proper layout behavior when React Native views are rendered inside Jetpack Compose components. It syncs layout information from Jetpack Compose back to React Native's Yoga layout system by updating the shadow node size.

When React Native views are placed inside Jetpack Compose components like [`ModalBottomSheet`](/versions/latest/sdk/ui/jetpack-compose/bottomsheet.md), [`Card`](/versions/latest/sdk/ui/jetpack-compose/card.md), [`Row`](/versions/latest/sdk/ui/jetpack-compose/row.md), [`Column`](/versions/latest/sdk/ui/jetpack-compose/column.md) and so on, the layout systems need to communicate. `RNHostView` bridges this gap:

-   **With [`matchContents`](/versions/latest/sdk/ui/jetpack-compose/rnhostview.md#matchcontents)**: The shadow node size is set to match the child React Native view's intrinsic size, allowing the Jetpack Compose parent to size itself based on the React Native content.
-   **Without `matchContents`**: The shadow node size is set to match the parent Jetpack Compose view's size, allowing the React Native content to fill the available space (useful for `flex: 1` layouts).

## Installation

```sh
# npm
npx expo install @expo/ui

# yarn
yarn expo install @expo/ui

# pnpm
pnpm expo install @expo/ui

# bun
bun expo install @expo/ui
```

If you are installing this in an [existing React Native app](/bare/overview.md), make sure to [install `expo`](/bare/installing-expo-modules.md) in your project.

## Usage

### Basic usage with matchContents

Use `matchContents` when you want the Jetpack Compose parent to size itself based on the React Native content.

```tsx
import { useState } from 'react';
import { Pressable, Text as RNText, View } from 'react-native';
import { Host, Card, Column, Row, RNHostView, Text } from '@expo/ui/jetpack-compose';
import { fillMaxWidth, padding } from '@expo/ui/jetpack-compose/modifiers';

function Example() {
  const [counter, setCounter] = useState(0);

  return (
    <Host style={{ flex: 1 }}>
      <Card modifiers={[fillMaxWidth()]}>
        <Column verticalArrangement={{ spacedBy: 12 }} modifiers={[padding(16, 16, 16, 16)]}>
          <Text>Mixing RN Components with Compose</Text>
          <Row horizontalArrangement={{ spacedBy: 24 }} verticalAlignment="center">
            <RNHostView matchContents>
              <Pressable
                onPress={() => setCounter(prev => prev - 1)}
                style={{
                  height: 50,
                  width: 50,
                  borderRadius: 100,
                  justifyContent: 'center',
                  alignItems: 'center',
                  backgroundColor: '#9B59B6',
                }}>
                <RNText style={{ color: 'white', fontSize: 24 }}>-</RNText>
              </Pressable>
            </RNHostView>
            <Text>{counter}</Text>
            <RNHostView matchContents>
              <Pressable
                onPress={() => setCounter(prev => prev + 1)}
                style={{
                  height: 50,
                  width: 50,
                  borderRadius: 100,
                  justifyContent: 'center',
                  alignItems: 'center',
                  backgroundColor: '#9B59B6',
                }}>
                <RNText style={{ color: 'white', fontSize: 24 }}>+</RNText>
              </Pressable>
            </RNHostView>
          </Row>
        </Column>
      </Card>
    </Host>
  );
}
```

### Flexible content without matchContents

When using `flex: 1` in your React Native content, omit the `matchContents` prop so the content fills the available Jetpack Compose space.

```tsx
import { Text as RNText, View } from 'react-native';
import { Host, Card, Column, Row, RNHostView, Text } from '@expo/ui/jetpack-compose';
import { fillMaxWidth, padding, size } from '@expo/ui/jetpack-compose/modifiers';

function Example() {
  return (
    <Host style={{ flex: 1 }}>
      <Card modifiers={[fillMaxWidth()]}>
        <Column verticalArrangement={{ spacedBy: 12 }} modifiers={[padding(16, 16, 16, 16)]}>
          <Text>RN components with flex: 1 children</Text>
          <Row horizontalArrangement={{ spacedBy: 20 }} modifiers={[size(100, 100)]}>
            <RNHostView>
              <View
                style={{
                  flex: 1,
                  backgroundColor: '#9B59B6',
                  borderRadius: 10,
                }}
              />
            </RNHostView>
          </Row>
        </Column>
      </Card>
    </Host>
  );
}
```

### Usage with ModalBottomSheet

`RNHostView` works well inside [`ModalBottomSheet`](/versions/latest/sdk/ui/jetpack-compose/bottomsheet.md) to display interactive React Native content.

```tsx
import { useRef, useState } from 'react';
import { Pressable, Text as RNText, View } from 'react-native';
import { Host, ModalBottomSheet, Button, Column, RNHostView, Text } from '@expo/ui/jetpack-compose';
import type { ModalBottomSheetRef } from '@expo/ui/jetpack-compose';
import { padding } from '@expo/ui/jetpack-compose/modifiers';

function Example() {
  const [visible, setVisible] = useState(false);
  const sheetRef = useRef<ModalBottomSheetRef>(null);

  const hideSheet = async () => {
    await sheetRef.current?.hide();
    setVisible(false);
  };

  return (
    <Host matchContents>
      <Button onClick={() => setVisible(true)}>
        <Text>Open Sheet</Text>
      </Button>
      {visible && (
        <ModalBottomSheet ref={sheetRef} onDismissRequest={() => setVisible(false)}>
          <Column verticalArrangement={{ spacedBy: 16 }} modifiers={[padding(16, 16, 16, 16)]}>
            <Text>Mixing Compose + RN in a Bottom Sheet</Text>
            <RNHostView matchContents>
              <View>
                <RNText style={{ fontSize: 18, fontWeight: 'bold', marginBottom: 8 }}>
                  React Native Content
                </RNText>
                <Pressable
                  style={{
                    backgroundColor: '#007AFF',
                    padding: 12,
                    borderRadius: 8,
                    alignItems: 'center',
                  }}
                  onPress={hideSheet}>
                  <RNText style={{ color: 'white', fontWeight: '600' }}>Close</RNText>
                </Pressable>
              </View>
            </RNHostView>
          </Column>
        </ModalBottomSheet>
      )}
    </Host>
  );
}
```

### Flexible React Native content in a bottom sheet

Use `RNHostView` without `matchContents` to let the React Native view fill the remaining space inside the sheet. Combine with a `height` modifier on the parent `Column` to control the sheet size.

```tsx
import { useRef, useState } from 'react';
import { Text as RNText, View } from 'react-native';
import { Host, ModalBottomSheet, Button, Column, RNHostView, Text } from '@expo/ui/jetpack-compose';
import type { ModalBottomSheetRef } from '@expo/ui/jetpack-compose';
import { height, padding } from '@expo/ui/jetpack-compose/modifiers';

function Example() {
  const [visible, setVisible] = useState(false);
  const sheetRef = useRef<ModalBottomSheetRef>(null);

  return (
    <Host matchContents>
      <Button onClick={() => setVisible(true)}>
        <Text>Open Flex Content Sheet</Text>
      </Button>
      {visible && (
        <ModalBottomSheet
          ref={sheetRef}
          onDismissRequest={() => setVisible(false)}
          skipPartiallyExpanded>
          <Column modifiers={[height(400), padding(16, 16, 16, 16)]}>
            <RNHostView>
              <View style={{ flex: 1, backgroundColor: '#9B59B6', borderRadius: 10 }}>
                <RNText
                  style={{
                    color: 'white',
                    fontSize: 18,
                    fontWeight: 'bold',
                    padding: 16,
                  }}>
                  React Native Content (flex: 1)
                </RNText>
              </View>
            </RNHostView>
          </Column>
        </ModalBottomSheet>
      )}
    </Host>
  );
}
```

## API

```tsx
import { RNHostView } from '@expo/ui/jetpack-compose';
```

## Component

### `RNHostView`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<RNHostProps\>

RNHostViewProps

### `children`

Supported platforms: Android.

Type: `ReactElement`

The RN View to be hosted.

### `matchContents`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `false`

When `true`, the RNHost will update its size in the Jetpack Compose view tree to match the children's size. When `false`, the RNHost will use the size of the parent Jetpack Compose View. Can be only set once on mount.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `style`

Supported platforms: Android.

Optional • Type: StyleProp<[ViewStyle](https://reactnative.dev/docs/view-style-props)\>

Style applied to the host view's React Native shadow node. Useful for controlling its layout position (e.g. `position: 'absolute'`) so the shadow layout matches where the hosting Compose component draws the content — important for `measure()`-based hit-testing such as `Pressable`.

#### Inherited Props

-   `PrimitiveBaseProps`
