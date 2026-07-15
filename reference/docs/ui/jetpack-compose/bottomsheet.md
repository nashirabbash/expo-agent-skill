---
title: "ModalBottomSheet"
description: "A Jetpack Compose ModalBottomSheet component that presents content from the bottom of the screen."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/bottomsheet.md"
scraped_at: "2026-07-15T09:00:49.814893"
---

---
title: ModalBottomSheet
description: A Jetpack Compose ModalBottomSheet component that presents content from the bottom of the screen.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# ModalBottomSheet

A Jetpack Compose ModalBottomSheet component that presents content from the bottom of the screen.
Android, Included in Expo Go

> For cross-platform usage, see the universal [`BottomSheet`](/versions/latest/sdk/ui/universal/bottomsheet.md) — it renders the appropriate native component per platform.

Expo UI ModalBottomSheet matches the official Jetpack Compose [Bottom Sheet API](https://developer.android.com/develop/ui/compose/components/bottom-sheets) and displays content in a modal sheet that slides up from the bottom.

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

### Basic bottom sheet

Use `ref.hide()` to programmatically dismiss the sheet with an animation before unmounting it.

```tsx
import { useRef, useState } from 'react';
import { Host, ModalBottomSheet, Button, Column, Text } from '@expo/ui/jetpack-compose';
import type { ModalBottomSheetRef } from '@expo/ui/jetpack-compose';
import { paddingAll } from '@expo/ui/jetpack-compose/modifiers';

export default function BasicBottomSheetExample() {
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
          <Column verticalArrangement={{ spacedBy: 12 }} modifiers={[paddingAll(24)]}>
            <Text>Hello from bottom sheet!</Text>
            <Text>You can add more content here.</Text>
            <Button onClick={hideSheet}>
              <Text>Close</Text>
            </Button>
          </Column>
        </ModalBottomSheet>
      )}
    </Host>
  );
}
```

### Skip partially expanded state

When `skipPartiallyExpanded` is set, the sheet opens directly in the fully expanded state instead of stopping at the half-height position first.

```tsx
import { useRef, useState } from 'react';
import { Host, ModalBottomSheet, Button, Column, Text } from '@expo/ui/jetpack-compose';
import type { ModalBottomSheetRef } from '@expo/ui/jetpack-compose';
import { paddingAll, height } from '@expo/ui/jetpack-compose/modifiers';

export default function SkipPartiallyExpandedExample() {
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
        <ModalBottomSheet
          ref={sheetRef}
          onDismissRequest={() => setVisible(false)}
          skipPartiallyExpanded>
          <Column verticalArrangement={{ spacedBy: 12 }} modifiers={[paddingAll(24), height(600)]}>
            <Text>This sheet skips the partially expanded state.</Text>
            <Text>It opens directly in the fully expanded position.</Text>
            <Button onClick={hideSheet}>
              <Text>Close</Text>
            </Button>
          </Column>
        </ModalBottomSheet>
      )}
    </Host>
  );
}
```

### Initial fully expanded state

When `initialFullyExpanded` is `true`, the sheet opens directly in the fully expanded state on first composition while leaving the partial state reachable. Unlike `skipPartiallyExpanded`, the user can still drag down to the partial state. The `partialExpand()` method also continues to work.

```tsx
import { useRef, useState } from 'react';
import { Host, ModalBottomSheet, Button, Column, Text } from '@expo/ui/jetpack-compose';
import type { ModalBottomSheetRef } from '@expo/ui/jetpack-compose';
import { paddingAll } from '@expo/ui/jetpack-compose/modifiers';

export default function InitialFullyExpandedExample() {
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
        <ModalBottomSheet
          ref={sheetRef}
          onDismissRequest={() => setVisible(false)}
          initialFullyExpanded>
          <Column verticalArrangement={{ spacedBy: 12 }} modifiers={[paddingAll(24)]}>
            <Text>This sheet opened fully expanded.</Text>
            <Text>You can still drag it down to the partial state.</Text>
            <Button onClick={() => sheetRef.current?.partialExpand()}>
              <Text>Collapse to partial</Text>
            </Button>
            <Button onClick={hideSheet}>
              <Text>Close</Text>
            </Button>
          </Column>
        </ModalBottomSheet>
      )}
    </Host>
  );
}
```

### Custom colors

Use `containerColor`, `contentColor`, and `scrimColor` to customize the sheet's appearance.

```tsx
import { useRef, useState } from 'react';
import { Host, ModalBottomSheet, Button, Column, Text } from '@expo/ui/jetpack-compose';
import type { ModalBottomSheetRef } from '@expo/ui/jetpack-compose';
import { paddingAll } from '@expo/ui/jetpack-compose/modifiers';

export default function CustomColorsExample() {
  const [visible, setVisible] = useState(false);
  const sheetRef = useRef<ModalBottomSheetRef>(null);

  const hideSheet = async () => {
    await sheetRef.current?.hide();
    setVisible(false);
  };

  return (
    <Host matchContents>
      <Button onClick={() => setVisible(true)}>
        <Text>Open Colored Sheet</Text>
      </Button>
      {visible && (
        <ModalBottomSheet
          ref={sheetRef}
          onDismissRequest={() => setVisible(false)}
          containerColor="#1a1a2e"
          contentColor="#e0e0e0"
          scrimColor="#806200EE">
          <Column verticalArrangement={{ spacedBy: 12 }} modifiers={[paddingAll(24)]}>
            <Text>Custom styled bottom sheet.</Text>
            <Text>Dark container with a purple scrim overlay.</Text>
            <Button onClick={hideSheet}>
              <Text>Close</Text>
            </Button>
          </Column>
        </ModalBottomSheet>
      )}
    </Host>
  );
}
```

### Custom drag handle

Use `ModalBottomSheet.DragHandle` slot to provide a custom drag handle, or set `showDragHandle={false}` to hide it entirely.

```tsx
import { useRef, useState } from 'react';
import { Host, ModalBottomSheet, Button, Column, Box, Text } from '@expo/ui/jetpack-compose';
import type { ModalBottomSheetRef } from '@expo/ui/jetpack-compose';
import {
  background,
  clip,
  fillMaxWidth,
  height,
  padding,
  Shapes,
  width,
} from '@expo/ui/jetpack-compose/modifiers';

export default function CustomDragHandleExample() {
  const [visible, setVisible] = useState(false);
  const sheetRef = useRef<ModalBottomSheetRef>(null);

  const hideSheet = async () => {
    await sheetRef.current?.hide();
    setVisible(false);
  };

  return (
    <Host matchContents>
      <Button onClick={() => setVisible(true)}>
        <Text>Open Custom Handle Sheet</Text>
      </Button>
      {visible && (
        <ModalBottomSheet ref={sheetRef} onDismissRequest={() => setVisible(false)}>
          <ModalBottomSheet.DragHandle>
            <Column horizontalAlignment="center" modifiers={[fillMaxWidth(), padding(0, 12, 0, 8)]}>
              <Box modifiers={[width(60), height(6), clip(Shapes.Circle), background('#6200EE')]} />
            </Column>
          </ModalBottomSheet.DragHandle>
          <Column verticalArrangement={{ spacedBy: 12 }} modifiers={[padding(16, 16, 16, 16)]}>
            <Button onClick={hideSheet}>
              <Text>Close</Text>
            </Button>
          </Column>
        </ModalBottomSheet>
      )}
    </Host>
  );
}
```

### React Native content inside a bottom sheet

Use `RNHostView` to embed interactive React Native views inside a Compose bottom sheet. This lets you mix Compose layout with RN components like `Pressable` and `Text`.

```tsx
import { useRef, useState } from 'react';
import { Host, ModalBottomSheet, Button, Column, RNHostView, Text } from '@expo/ui/jetpack-compose';
import type { ModalBottomSheetRef } from '@expo/ui/jetpack-compose';
import { padding } from '@expo/ui/jetpack-compose/modifiers';
import { Pressable, Text as RNText, View } from 'react-native';

export default function RNContentBottomSheetExample() {
  const [visible, setVisible] = useState(false);
  const sheetRef = useRef<ModalBottomSheetRef>(null);

  const hideSheet = async () => {
    await sheetRef.current?.hide();
    setVisible(false);
  };

  return (
    <Host matchContents>
      <Button onClick={() => setVisible(true)}>
        <Text>Open RN Content Sheet</Text>
      </Button>
      {visible && (
        <ModalBottomSheet
          ref={sheetRef}
          onDismissRequest={() => setVisible(false)}
          skipPartiallyExpanded={false}>
          <Column verticalArrangement={{ spacedBy: 16 }} modifiers={[padding(16, 16, 16, 16)]}>
            <Text>Mixing Compose + RN in a Bottom Sheet</Text>
            <RNHostView>
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

### React Native content with flex

Use `RNHostView` without `matchContents` to let the RN view fill the remaining space inside the sheet. Combine with a fixed `height` modifier on the parent `Column` to control the sheet size.

```tsx
import { useRef, useState } from 'react';
import { Host, ModalBottomSheet, Button, Column, RNHostView, Text } from '@expo/ui/jetpack-compose';
import type { ModalBottomSheetRef } from '@expo/ui/jetpack-compose';
import { height, padding } from '@expo/ui/jetpack-compose/modifiers';
import { Text as RNText, View } from 'react-native';

export default function FlexRNContentExample() {
  const [visible, setVisible] = useState(false);
  const sheetRef = useRef<ModalBottomSheetRef>(null);

  const hideSheet = async () => {
    await sheetRef.current?.hide();
    setVisible(false);
  };

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
            <Text>RN View with flex: 1</Text>
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

### Scrollable React Native content

Nest a scrollable React Native list such as `FlatList`, `ScrollView`, or a high-performance list like [FlashList](https://shopify.github.io/flash-list/) or [Legend List](https://github.com/LegendApp/legend-list) inside the sheet with `RNHostView`. Set `nestedScrollEnabled` on the scrollable so it scrolls its own content first. Once it reaches the top edge, the remaining drag moves the sheet. Without `nestedScrollEnabled` the list consumes the gesture and the sheet stays put.

```tsx
import { useState } from 'react';
import { Host, ModalBottomSheet, Button, Column, RNHostView, Text } from '@expo/ui/jetpack-compose';
import { fillMaxHeight, padding } from '@expo/ui/jetpack-compose/modifiers';
import { FlatList, Text as RNText } from 'react-native';

const DATA = Array.from({ length: 50 }, (_, i) => `Item ${i + 1}`);

export default function ScrollableContentBottomSheetExample() {
  const [visible, setVisible] = useState(false);

  return (
    <Host matchContents>
      <Button onClick={() => setVisible(true)}>
        <Text>Open Scrollable Sheet</Text>
      </Button>
      {visible && (
        <ModalBottomSheet onDismissRequest={() => setVisible(false)}>
          <Column modifiers={[fillMaxHeight(), padding(16, 16, 16, 16)]}>
            <RNHostView>
              <FlatList
                nestedScrollEnabled
                style={{ flex: 1 }}
                data={DATA}
                keyExtractor={item => item}
                renderItem={({ item }) => <RNText style={{ paddingVertical: 16 }}>{item}</RNText>}
              />
            </RNHostView>
          </Column>
        </ModalBottomSheet>
      )}
    </Host>
  );
}
```

### Non-dismissible sheet

Combine `properties`, `sheetGesturesEnabled` to create a sheet that can only be closed programmatically.

```tsx
import { useRef, useState } from 'react';
import { Host, ModalBottomSheet, Button, Column, Text } from '@expo/ui/jetpack-compose';
import type { ModalBottomSheetRef } from '@expo/ui/jetpack-compose';
import { paddingAll } from '@expo/ui/jetpack-compose/modifiers';

export default function NonDismissibleExample() {
  const [visible, setVisible] = useState(false);
  const sheetRef = useRef<ModalBottomSheetRef>(null);

  const hideSheet = async () => {
    await sheetRef.current?.hide();
    setVisible(false);
  };

  return (
    <Host matchContents>
      <Button onClick={() => setVisible(true)}>
        <Text>Open Non-Dismissible Sheet</Text>
      </Button>
      {visible && (
        <ModalBottomSheet
          ref={sheetRef}
          onDismissRequest={() => setVisible(false)}
          sheetGesturesEnabled={false}
          properties={{
            shouldDismissOnBackPress: false,
            shouldDismissOnClickOutside: false,
          }}>
          <Column verticalArrangement={{ spacedBy: 12 }} modifiers={[paddingAll(24)]}>
            <Text>This sheet cannot be dismissed by swiping, back press, or tapping outside.</Text>
            <Text>Only the button below will close it.</Text>
            <Button onClick={hideSheet}>
              <Text>Close</Text>
            </Button>
          </Column>
        </ModalBottomSheet>
      )}
    </Host>
  );
}
```

## API

```tsx
import { ModalBottomSheet } from '@expo/ui/jetpack-compose';
```

## Constants

### `BottomSheet.ModalBottomSheet`

Supported platforms: Android.

Type: `ModalBottomSheetComponent`

## Props

### `children`

Supported platforms: Android.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

The children of the `ModalBottomSheet` component. Can include a `ModalBottomSheet.DragHandle` slot for a custom drag handle.

### `containerColor`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The background color of the bottom sheet.

### `contentColor`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The preferred color of the content inside the bottom sheet.

### `initialFullyExpanded`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `false`

Opens the sheet fully expanded on first composition. Ignored when `skipPartiallyExpanded` is `true`.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onDismissRequest`

Supported platforms: Android.

Type: `() => void`

Callback function that is called when the user dismisses the bottom sheet (via swipe, back press, or tapping outside the scrim).

### `properties`

Supported platforms: Android.

Optional • Type: [ModalBottomSheetProperties](#modalbottomsheetproperties)

Properties for the modal window behavior.

### `ref`

Supported platforms: Android.

Optional • Type: Ref<[ModalBottomSheetRef](#modalbottomsheetref)\>

Can be used to imperatively hide the bottom sheet with an animation.

### `scrimColor`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The color of the scrim overlay behind the bottom sheet.

### `sheetGesturesEnabled`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `true`

Whether gestures (swipe to dismiss) are enabled on the bottom sheet.

### `showDragHandle`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `true`

Whether to show the default drag handle at the top of the bottom sheet. Ignored if a custom `ModalBottomSheet.DragHandle` slot is provided.

### `skipPartiallyExpanded`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `false`

Immediately opens the bottom sheet in full screen.

## Types

### `ModalBottomSheetProperties`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| shouldDismissOnBackPress(optional) | `boolean` | Whether the bottom sheet can be dismissed by pressing the back button. Default: `true` |
| shouldDismissOnClickOutside(optional) | `boolean` | Whether the bottom sheet can be dismissed by clicking outside (on the scrim). Default: `true` |

### `ModalBottomSheetRef`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| expand | () => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | Programmatically expands the bottom sheet to full height with an animation. |
| hide | () => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | Programmatically hides the bottom sheet with an animation. The returned promise resolves after the dismiss animation completes. |
| partialExpand | () => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | Programmatically collapses the bottom sheet to partially expanded (~50%) state. Only works when `skipPartiallyExpanded` is `false`. |
